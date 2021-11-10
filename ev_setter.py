class EnvironmentVariables(object):
    FLASK_APP = 'microblog.py'
    FLASK_DEBUG = 1


ev = EnvironmentVariables()
ev_list = [a for a in dir(ev) if not a.startswith('__')]


def quotes(variable):
    return "'" if type(getattr(ev, variable)) == str else ''


# PowerShell
ev_lines = ['$env:{0} = {1}{2}{1}'.format(variable,
                                          quotes(variable),
                                          getattr(ev, variable)) for variable in ev_list]


# Clear unused ev
def clear_ev_lines(file, searchExp):
    with open(file, 'r') as f:
        new_lines = f.readlines()

        for key, new_line in enumerate(reversed(new_lines)):
            if searchExp in new_line:
                new_lines[len(new_lines) - 1 - key] = ''
            elif new_line == '':
                continue
            else:
                break

    with open(file, 'w') as f:
        f.writelines(new_lines)


# Add new ev
def add_ev_lines(file, new_lines):
    with open(file, 'a') as f:
        for line in new_lines:
            f.write(line + '\n')


clear_ev_lines('venv/Scripts/activate.ps1', '$env:')
add_ev_lines('venv/Scripts/activate.ps1', ev_lines)
