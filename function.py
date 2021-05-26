import re
import pathlib

def function():
    with open("program.bsl", "r+") as f:
        try:
            for k, i in enumerate(f):
                if (':=' in i) and not ('!' in i) and not ('while' in i) and not ('do' in i) and not ('if' in i):
                    nums = re.findall('(\d+)', i)
                    path = pathlib.Path('program.bsl')
                    result = i.replace(' ', '')
                    if '^' in result:
                        result = result.replace('^', '**')

                    path.write_text(path.read_text().replace(i, i[:i.index(nums[0])] +
                                                             str(eval(result[3:])) + '\n'))
        except Exception as e:
            print("Exception {}".format(e))