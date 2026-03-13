#!/usr/bin/env python3
"""
Explore taxonomic classification counts for invertebrates in GBIF occurrence data.
Filters for Animalia kingdom excluding Chordata (vertebrates).
"""

import pandas as pd
import argparse
from pathlib import Path
from collections import Counter


def load_and_filter_invertebrates(csv_path, chunksize=50000):
    """
    Load CSV in chunks and filter for invertebrates.
    Invertebrates = Animalia kingdom, excluding Chordata phylum.
    """
    print(f"Loading data from: {csv_path}")
    print(f"Processing in chunks of {chunksize} rows...")

    invertebrate_chunks = []
    total_rows = 0
    invertebrate_rows = 0

    # Read CSV in chunks to handle large files
    for chunk_num, chunk in enumerate(pd.read_csv(csv_path, chunksize=chunksize, low_memory=False), 1):
        total_rows += len(chunk)

        # Filter for invertebrates: Animalia kingdom, not Chordata phylum
        invertebrates = chunk[
            (chunk['kingdom'] == 'Animalia') &
            (chunk['phylum'] != 'Chordata')
        ]

        invertebrate_rows += len(invertebrates)
        invertebrate_chunks.append(invertebrates)

        if chunk_num % 10 == 0:
            print(f"  Processed {total_rows:,} rows, found {invertebrate_rows:,} invertebrates...")

    print(f"\nTotal rows processed: {total_rows:,}")
    print(f"Total invertebrates found: {invertebrate_rows:,}")

    # Combine all chunks
    if invertebrate_chunks:
        return pd.concat(invertebrate_chunks, ignore_index=True)
    else:
        return pd.DataFrame()


def analyze_taxonomy(df):
    """Analyze and display taxonomic counts at different levels."""

    print("\n" + "="*80)
    print("TAXONOMIC CLASSIFICATION ANALYSIS FOR INVERTEBRATES")
    print("="*80)

    # Kingdom counts
    print("\n--- KINGDOM ---")
    kingdom_counts = df['kingdom'].value_counts()
    for kingdom, count in kingdom_counts.items():
        print(f"  {kingdom}: {count:,}")

    # Phylum counts
    print("\n--- PHYLUM ---")
    phylum_counts = df['phylum'].value_counts()
    print(f"Total unique phyla: {len(phylum_counts)}")
    for phylum, count in phylum_counts.head(20).items():
        pct = (count / len(df)) * 100
        print(f"  {phylum}: {count:,} ({pct:.2f}%)")

    if len(phylum_counts) > 20:
        print(f"  ... and {len(phylum_counts) - 20} more phyla")

    # Class counts
    print("\n--- CLASS ---")
    class_counts = df['class'].value_counts()
    print(f"Total unique classes: {len(class_counts)}")
    for cls, count in class_counts.head(30).items():
        pct = (count / len(df)) * 100
        print(f"  {cls}: {count:,} ({pct:.2f}%)")

    if len(class_counts) > 30:
        print(f"  ... and {len(class_counts) - 30} more classes")

    # Order counts
    print("\n--- ORDER ---")
    order_counts = df['order'].value_counts()
    print(f"Total unique orders: {len(order_counts)}")
    for order, count in order_counts.head(40).items():
        pct = (count / len(df)) * 100
        print(f"  {order}: {count:,} ({pct:.2f}%)")

    if len(order_counts) > 40:
        print(f"  ... and {len(order_counts) - 40} more orders")

    return {
        'kingdom': kingdom_counts,
        'phylum': phylum_counts,
        'class': class_counts,
        'order': order_counts
    }


def save_results(counts_dict, output_dir):
    """Save taxonomic counts to CSV files."""
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    print(f"\n--- SAVING RESULTS TO {output_dir} ---")

    for level, counts in counts_dict.items():
        filename = output_path / f"invertebrate_{level}_counts.csv"
        counts_df = pd.DataFrame({
            level: counts.index,
            'count': counts.values,
            'percentage': (counts.values / counts.sum() * 100).round(2)
        })
        counts_df.to_csv(filename, index=False)
        print(f"  Saved {filename}")


def explore_phylum(df, phylum_name):
    """Explore a specific phylum in detail."""
    phylum_data = df[df['phylum'] == phylum_name]

    if len(phylum_data) == 0:
        print(f"\nNo records found for phylum: {phylum_name}")
        return

    print(f"\n{'='*80}")
    print(f"DETAILED BREAKDOWN FOR PHYLUM: {phylum_name}")
    print(f"{'='*80}")
    print(f"Total records: {len(phylum_data):,}")

    print(f"\nClasses in {phylum_name}:")
    class_counts = phylum_data['class'].value_counts()
    for cls, count in class_counts.items():
        pct = (count / len(phylum_data)) * 100
        print(f"  {cls}: {count:,} ({pct:.2f}%)")

    print(f"\nOrders in {phylum_name}:")
    order_counts = phylum_data['order'].value_counts()
    for order, count in order_counts.head(30).items():
        pct = (count / len(phylum_data)) * 100
        print(f"  {order}: {count:,} ({pct:.2f}%)")

    if len(order_counts) > 30:
        print(f"  ... and {len(order_counts) - 30} more orders")


def main():
    parser = argparse.ArgumentParser(
        description='Explore taxonomic classification of invertebrates in GBIF data'
    )
    parser.add_argument(
        '--csv',
        default='source-data/0049395-241126133413365/occurrence.csv',
        help='Path to occurrence.csv file'
    )
    parser.add_argument(
        '--output',
        default='output/taxonomy_analysis',
        help='Output directory for CSV results'
    )
    parser.add_argument(
        '--phylum',
        help='Explore a specific phylum in detail (e.g., Arthropoda, Mollusca)'
    )
    parser.add_argument(
        '--chunksize',
        type=int,
        default=50000,
        help='Number of rows to process at a time (default: 50000)'
    )

    args = parser.parse_args()

    # Load and filter data
    df = load_and_filter_invertebrates(args.csv, chunksize=args.chunksize)

    if df.empty:
        print("No invertebrate data found!")
        return

    # Analyze taxonomy
    counts = analyze_taxonomy(df)

    # Save results
    save_results(counts, args.output)

    # Explore specific phylum if requested
    if args.phylum:
        explore_phylum(df, args.phylum)

    print("\n" + "="*80)
    print("Analysis complete!")
    print("="*80)


if __name__ == '__main__':
    main()
