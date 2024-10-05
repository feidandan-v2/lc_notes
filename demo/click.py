
import click


@click.command()
@click.option(
    '-a',
    '--arg_1',
    type = str,
    default='Tom',
    help='参数1，人名')
@click.option(
    '-e',
    '--enable_x',
    type = bool,
    default=False,
    help='开启x功能')
def run(arg_1:str, enable_x:bool) -> None:
    """..."""
    name = arg_1

    if enable_x:
        print(f"{name} turns on X")
    else:
        print(f"{name} turns off X")

    return



if __name__ == "__main__":
    run()
