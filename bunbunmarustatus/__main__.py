import sys
import time
import bunbunmarustatus as bun


def main():
    pattern = "time"

    if "-c" not in sys.argv:
        if "--laptop" in sys.argv:
            pattern = "battery time"

        if "--pulse" in sys.argv:
            pattern = "pulse " + pattern

        if "--mpd" in sys.argv:
            pattern = "mpd " + pattern

    else:
        i = sys.argv.index("-c")
        pattern = sys.argv[i + 1]

    try:
        interval = int(sys.argv[1])
    except:
        interval = 5

    status = bun.Status(pattern)

    bun.factory(status)

    sys.stdout.write('{"version":1}\n')
    sys.stdout.flush()
    sys.stdout.write("[\n")
    sys.stdout.flush()

    while True:
        sys.stdout.write(status.get_status() + ",\n")
        sys.stdout.flush()
        time.sleep(interval)


if __name__ == "__main__":
    main()
