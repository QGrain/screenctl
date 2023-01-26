import argparse
import os, sys
import json
import re
from time import sleep
from . import NAME, VERSION, DESCRIPTION


class ProgressBar(object):
    DEFAULT = 'Progress: %(bar)s %(percent)3d%%'
    FULL = '%(bar)s %(current)d/%(total)d (%(percent)3d%%) '

    def __init__(self, total, width=40, fmt=DEFAULT, symbol='=', output=sys.stderr):
        assert len(symbol) == 1

        self.total = total
        self.width = width
        self.symbol = symbol
        self.output = output
        self.fmt = re.sub(r'(?P<name>%\(.+?\))d', r'\g<name>%dd' % len(str(total)), fmt)
        self.current = 0

    def __call__(self):
        percent = self.current / float(self.total)
        size = int(self.width * percent)
        bar = '[' + self.symbol * size + ' ' * (self.width - size) + ']'

        args = {
            'total': self.total,
            'bar': bar,
            'current': self.current,
            'percent': percent * 100
        }
        print('\r' + self.fmt % args, file=self.output, end='')

    def done(self):
        self.current = self.total
        self()
        print('', file=self.output)


class ScreenCtl():
    def __init__(self, verbose):
        self.verbose = verbose
    
    def readConf(self, conf_path):
        with open(conf_path, 'r', encoding='utf-8') as f:
            conf = json.load(f)
        self.conf = conf
        return conf
    
    def statScreen(self, job):
        d = {}
        f = os.popen("screen -ls")
        ret = f.readlines()
        for line in ret:
            if job in line:
                line_split = line.split("\t")
                name = line_split[1].strip()
                create = line_split[2][1:-1]
                status = line_split[3].strip()[1:-1]

                job_name = name.split('.')[-1]
                cmd = ""
                for conf_job_name in self.conf:
                    if job_name == conf_job_name:
                        cmd = self.conf[conf_job_name]
                d[name] = {"create":create, "status":status, "cmd":cmd}
        f.close()
        return d

    def createScreen(self, job, cmd):
        stat = self.statScreen(job)
        if "\'" in cmd and "\"" in cmd:
            print("[WARN] \' and \" cannot show up in cmd at the same time")
            return {}
        elif "\"" in cmd:
            cmd = "\'" + cmd + "\\n" + "\'"
        else:
            cmd = "\"" + cmd + "\\n" + "\""

        if len(stat) == 0:
            # create screen as detached
            os.system("screen -dm %s"%job)
            # execute cmd in screen
            whole_cmd = "screen -x -S %s -X stuff %s"%(job, cmd)
            if self.verbose == True:
                print("whole_cmd:", whole_cmd)
            os.system(whole_cmd)
            return self.statScreen(job)
        else:
            print("[WARN] There are already %d screen named %s, please change another job name"%(len(stat), job))
            print_dict(stat)
            return {}


    def deleteScreen(self, job):
        stat = self.statScreen(job)
        for name in stat:
            f = os.popen("screen -r %s -X quit"%name)
            print(f.read())
            f.close()

def print_dict(d):
    if d == {}:
        print("[WARN] dict is blank")
    else:
        print(json.dumps(d, sort_keys=False, indent=4, ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("action", type=str, help='create, delete, stat, server')
    parser.add_argument("-c", "--conf", type=str, help='path to configuration')
    parser.add_argument('-v', '--verbose', help='show verbose output', action='store_true')
    args = parser.parse_args()

    verbose = args.verbose
    if args.conf:
        conf_path = args.conf
    else:
        # default configuration path
        conf_path = "./job.json"

    screenctl = ScreenCtl(verbose)
    conf = screenctl.readConf(conf_path)
    print_dict(conf)
    print("---------------------------------------")

    if args.action == "server":
        print("Run as a web server, todo...")

    progress = ProgressBar(len(conf), fmt=ProgressBar.FULL)

    for job in conf:
        progress.current += 1
        progress()
        sleep(0.2)
        if args.action == "create":
            screenctl.createScreen(job, conf[job])
        elif args.action == "delete":
            screenctl.deleteScreen(job)
            if verbose == True:
                print("delete job %s"%job)
        elif args.action == "stat":
            d = screenctl.statScreen(job)
            if verbose == True:
                print_dict(d)
    print("Done!")

if __name__ == "__main__":
    main()