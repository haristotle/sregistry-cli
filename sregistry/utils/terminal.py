'''

Copyright (C) 2017 The Board of Trustees of the Leland Stanford Junior
University.
Copyright (C) 2017 Vanessa Sochat.

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public
License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''


def check_install(software=None, quiet=True):
    '''check_install will attempt to run the singularity command, and
       return True if installed. The command line utils will not run 
       without this check.
    '''
    if software is None:
        software = "singularity"
    cmd = [software, '--version']
    try:
        version = run_command(cmd,software)
    except: # FileNotFoundError
        return False
    if version is not None:
        if quiet is False and version['return_code'] == 0:
            version = version['message']
            bot.info("Found %s version %s" % (software.upper(), version))
        return True 
    return False


def get_installdir():
    '''get_installdir returns the installation directory of the application
    '''
    return os.path.abspath(os.path.dirname(__file__))


def run_command(cmd, sudo=False):
    '''run_command uses subprocess to send a command to the terminal.
    :param cmd: the command to send, should be a list for subprocess
    :param error_message: the error message to give to user if fails,
    if none specified, will alert that command failed.
    :param sudopw: if specified (not None) command will be run asking for sudo
    '''
    if sudo is True:
        cmd = ['sudo'] + cmd

    output = Popen(cmd,stderr=STDOUT,stdout=PIPE)
    t = output.communicate()[0],output.returncode
    output = {'message':t[0],
              'return_code':t[1]}

    return output
