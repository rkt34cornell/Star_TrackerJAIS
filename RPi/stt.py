import argparse
import stt_selector as stt

parser = argparse.ArgumentParser(prog="STT", description="STT main script")
parser.add_argument("type", type=str, choices=["direct_rpi", "sample_rpi", "sample_stereo", "custom"],
                    help="Running mode: direct_rpi, sample_rpi, sample_stereo, or custom")
parser.add_argument("catalog", type=int, help="Catalog division: 5, 10, or 15")
parser.add_argument("-exp", "--exptime", type=int, default=800, help="Exposure time for direct mode")
parser.add_argument("-n", "--npic", type=int, default=1, help="Image number for sample modes")
parser.add_argument("-f", "--file", type=str, help="Full path to custom .fts file")

args = parser.parse_args()

if args.catalog not in (5, 10, 15):
    parser.error("Catalog division must be 5, 10, or 15")

if args.type == "direct_rpi":
    stt.solve_lis_grab_img(args.catalog, args.exptime)
elif args.type == "sample_rpi":
    stt.solve_lis_sample_rpi(args.catalog, args.npic)
elif args.type == "sample_stereo":
    stt.solve_lis_sample_stereo(args.catalog, args.npic)
elif args.type == "custom":
    if not args.file:
        parser.error("Please specify the file path using --file for custom mode.")
    stt.solve_lis_custom(args.catalog, args.file)
