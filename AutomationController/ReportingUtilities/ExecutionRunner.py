import getopt
import os
import platform
import sys
import time


def set_python_path():
    curr_dir = os.getcwd()
    if platform.system().lower() == "linux":
        os.system('export PYTHONPATH="${PYTHONPATH}:%s/../.."' % curr_dir)
    else:
        os.system('set PYTHONPATH="${PYTHONPATH}:%s/../.."' % curr_dir)


class ManageExecution:
    all_project_names = {}

    def __init__(self):
        self.arguments = {}
        self.epoch = int(time.time())
        set_python_path()

    def understand_arguments(self):
        try:
            opts, args = getopt.getopt(sys.argv[1:], "h:d:p:m:z:u:")
        except getopt.GetoptError:
            print('Please retry with correct command')
            sys.exit(1)

        for opt, arg in opts:
            if opt in ("-d", "--driverName"):
                self.arguments["driver"] = arg
            elif opt in ("-p", "--project_name"):
                self.arguments['project_name'] = arg
            elif opt in ("-z", "--platform"):
                self.arguments['platform'] = arg
            elif opt in ("-u", "--updateGS"):
                self.arguments['update_gs'] = arg

        if 'platform' not in self.arguments:
            print("Please provide platform to continue the execution")
            sys.exit(1)

        if 'project_name' not in self.arguments:
            print("Please provide Correct Project Name to continue the execution")
            sys.exit(1)

        if 'platform' in self.arguments and self.arguments["platform"].lower() != "web" and 'driver' in self.arguments:
            print("You do not need to pass driver when selected platform is not web")
            sys.exit(1)

        if self.arguments["platform"] == "web" and "driver" not in self.arguments:
            self.arguments['driver'] = "chrome"
            print("Note: You have not mentioned any browser name in command line arguments so execution will be running"
                  " on CHROME by default. If you wish to run on any other browser then please specify in command line "
                  "argument")
        return self.arguments

    def finalize_driver(self):
        arg = self.understand_arguments()
        if arg['platform'].lower() == "web":
            preferred_driver = arg['driver']
            os.environ["driver_to"] = preferred_driver

    def finalize_folder(self, arg):
        if arg['platform'].lower() == 'web':
            return '../../UI'
        elif arg['platform'].lower() == 'mobile':
            return '../UI/MobileAutomation'
        elif arg['platform'].lower() == 'api':
            return '../API/MobileAutomation'

    def finalize_project(self, arg):
        return "../../{}".format(arg["project_name"])

    def generate_run_command(self, arg):
        os.chdir(path="{}".format(self.finalize_project(arg=arg)))
        os.system("python main.py")


if __name__ == '__main__':
    manage = ManageExecution()
    manage.finalize_driver()
    manage.generate_run_command(manage.arguments)
