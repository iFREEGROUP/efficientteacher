
from argparse import ArgumentParser
from convert_pt_to_efficient import convert_efficient_to_yolov5, convert_yolov5_to_efficient
from pathlib import Path


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--cfg_path", type=Path,
                        help="""cfg path.""", default='')
    parser.add_argument("--efficient_path", type=Path,
                        help="""efficient pt path.""", default='')
    parser.add_argument("--yolov5_path", type=Path,
                        help="""此模型需要官方的原版模型""", default='')
    parser.add_argument("--save_path", type=Path,
                        help="""Save to local path.""", default='')
    parser.add_argument("--map_path", type=Path,  help="""Map Text path.""",
                        default='scripts/mula_convertor/map.txt')

    args = parser.parse_args()


    if args.cfg_path.is_file():
        convert_yolov5_to_efficient(
            args.yolov5_path,
            args.cfg_path,
            args.save_path,
            map_path=args.map_path,
        )

    else:
        convert_efficient_to_yolov5(
            efficient_path=args.efficient_path,
            yolov5_path=args.yolov5_path,
            save_path=args.save_path,
            map_path=args.map_path,
        )
