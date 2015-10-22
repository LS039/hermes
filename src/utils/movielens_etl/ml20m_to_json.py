#!/usr/bin/env python

import argparse

from movielens import ratings_to_json, tags_to_json, movies_to_json

# Set up command line flag handling
parser = argparse.ArgumentParser(
        description="Transform the MovieLens 20M dataset CSV files to JSON",
    )
parser.add_argument(
        'links_csv',
        type=str,
        help="the CSV file containing link data",
        )
parser.add_argument(
        'movies_csv',
        type=str,
        help="the CSV file containing movie data",
        )
parser.add_argument(
        'ratings_csv',
        type=str,
        help="the CSV file containing rating data",
        )
parser.add_argument(
        'tags_csv',
        type=str,
        help="the CSV file containing tag data",
        )
parser.add_argument(
        '-o',
        '--output_directory',
        type=str,
        action="store",
        help="the directory to save the output JSON files, by default the current directory",
        default="./",
        )


# Run only if this script is being called directly
if __name__ == "__main__":

    args = parser.parse_args()

    ratings_to_json(args.ratings_csv, args.output_directory)
    tags_to_json(args.tags_csv, args.output_directory)
    movies_to_json(args.movies_csv, args.links_csv, args.output_directory)
