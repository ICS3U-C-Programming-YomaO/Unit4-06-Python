#!/usr/bin/env python3
# Created By: Yoma Ozoh
# Date: November, 2025
# This program plays with colors


def main():
    # loop for red
    for red in range(0, 256, 1):
        # loop for blue
        for green in range(0, 256, 1):
            # loop for green
            for blue in range(0, 256, 1):
                # show the colors to user
                print(
                    f"\033[1;38;2;{red};{green};{blue}mRGB({red}, {green}, {blue})\033[0m"
                )


if __name__ == "__main__":
    main()
