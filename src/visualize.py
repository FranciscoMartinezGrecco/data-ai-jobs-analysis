"""
visualize.py — Reusable visualization functions.

All charts are publication-quality with proper titles, labels,
and color palettes. Each function can optionally save to file.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import os


# Global style settings
PALETTE = 'viridis'
FIGSIZE_WIDE = (12, 6)
FIGSIZE_SQUARE = (10, 8)
OUTPUT_DIR = os.path.join('..', 'outputs', 'figures')


def _save_fig(fig, filename: str, save: bool = True) -> None:
    """Save figure to outputs/figures/ if save=True."""
    if save and filename:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        filepath = os.path.join(OUTPUT_DIR, filename)
        fig.savefig(filepath, dpi=150, bbox_inches='tight')
        print(f"Saved: {filepath}")


def plot_salary_distribution(df, save=True):
    """KDE plot of salary distribution with mean and median lines."""
    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)

    sns.kdeplot(data=df, x='salary_in_usd', fill=True, alpha=0.3, ax=ax)

    mean_sal = df['salary_in_usd'].mean()
    median_sal = df['salary_in_usd'].median()

    ax.axvline(mean_sal, color='red', linestyle='--', label=f'Mean: ${mean_sal:,.0f}')
    ax.axvline(median_sal, color='green', linestyle='-', label=f'Median: ${median_sal:,.0f}')

    ax.set_title('Salary Distribution (USD)', fontsize=14, fontweight='bold')
    ax.set_xlabel('Annual Salary (USD)')
    ax.set_ylabel('Density')
    ax.legend()

    _save_fig(fig, 'salary_distribution.png', save)
    plt.show()


def plot_salary_by_role(df, top_n=10, save=True):
    """Horizontal bar plot of median salary by job title."""
    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)

    top_roles = (df.groupby('job_title')['salary_in_usd']
                 .median()
                 .sort_values(ascending=True)
                 .tail(top_n))

    top_roles.plot(kind='barh', ax=ax, color=sns.color_palette(PALETTE, top_n))

    ax.set_title(f'Top {top_n} Roles by Median Salary', fontsize=14, fontweight='bold')
    ax.set_xlabel('Median Salary (USD)')
    ax.set_ylabel('')

    _save_fig(fig, 'salary_by_role.png', save)
    plt.show()


def plot_salary_by_experience(df, save=True):
    """Boxplot with stripplot overlay for salary vs experience level."""
    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)

    order = ['Entry-Level', 'Mid-Level', 'Senior', 'Executive']
    sns.boxplot(data=df, x='experience_level', y='salary_in_usd',
                order=order, palette=PALETTE, ax=ax)
    sns.stripplot(data=df, x='experience_level', y='salary_in_usd',
                  order=order, color='black', alpha=0.3, size=3, ax=ax)

    ax.set_title('Salary by Experience Level', fontsize=14, fontweight='bold')
    ax.set_xlabel('Experience Level')
    ax.set_ylabel('Salary (USD)')

    _save_fig(fig, 'salary_by_experience.png', save)
    plt.show()


def plot_remote_trend(df, save=True):
    """Line plot showing salary trend by year and remote category."""
    fig, ax = plt.subplots(figsize=FIGSIZE_WIDE)

    if 'remote_category' not in df.columns:
        df = df.copy()
        df['remote_category'] = df['remote_ratio'].map({
            0: 'On-site', 50: 'Hybrid', 100: 'Remote'
        })

    trend = (df.groupby(['work_year', 'remote_category'])['salary_in_usd']
             .median()
             .reset_index())

    sns.lineplot(data=trend, x='work_year', y='salary_in_usd',
                 hue='remote_category', marker='o', ax=ax)

    ax.set_title('Median Salary Trend by Remote Category', fontsize=14, fontweight='bold')
    ax.set_xlabel('Year')
    ax.set_ylabel('Median Salary (USD)')

    _save_fig(fig, 'remote_salary_trend.png', save)
    plt.show()
