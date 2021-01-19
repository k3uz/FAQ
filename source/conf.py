# -*- coding: utf-8 -*-

# Fedora-Faq-Ru (c) 2018 - 2020, EasyCoding Team and contributors
#
# Fedora-Faq-Ru is licensed under a
# Creative Commons Attribution-ShareAlike 4.0 International License.
#
# You should have received a copy of the license along with this
# work. If not, see <https://creativecommons.org/licenses/by-sa/4.0/>.

# All configuration values have a default; values that are commented out
# serve to show the default.

# Importing some Python modules.
from os import getenv
from time import strftime

# Configuring version and Git snapshots.
rel_version = '2020.12.30'
rel_snapshot = getenv('CI_HASH')

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = '1.6'
keep_warnings = False

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.ifconfig',
    'sphinx.ext.githubpages']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Неофициальный FAQ по Fedora'
copyright = '2018 - {}, EasyCoding Team and contributors'.format(strftime('%Y'))
author = 'EasyCoding Team and contributors'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = 'git' if rel_snapshot else rel_version
# The full version, including alpha/beta/rc tags.
release = 'git~{}'.format(rel_snapshot) if rel_snapshot else rel_version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'ru'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# Load CSS files for the custom search engine.
html_css_files = [
    'https://cdn.jsdelivr.net/npm/docsearch.js@2/dist/cdn/docsearch.min.css'
]

# Load JavaScript files for the custom search engine.
html_js_files = [
    ('https://cdn.jsdelivr.net/npm/docsearch.js@2/dist/cdn/docsearch.min.js', {'defer': 'defer'}),
    ('search.js', {'defer': 'defer'})
]

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'font_family': 'sans-serif',
    'head_font_family': 'serif',
    'font_size': '16px',
    'show_powered_by': False,
    'github_user': 'RussianFedora',
    'github_repo': 'FAQ',
    'github_banner': 'forkme_right_green.png',
    'github_button': False,
    'logo': 'faq-icon.png',
    'touch_icon': 'faq-icon.png',
    'logo_name': False
}

# Override default HTML title for HTML and HTML Help pages.
html_title = '{} (версия {})'.format(project, version)

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'searchbox.html',
        'navigation.html',
        'relations.html'
    ]
}

# Add favicon for generated HTML pages.
html_favicon = '_static/faq-icon.ico'

# Other HTML options
html_copy_source = False
html_show_sourcelink = False
html_show_sphinx = False


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'fedora-faq-ru'


# -- Options for LaTeX output ---------------------------------------------

# For additional options see: https://www.sphinx-doc.org/en/master/latex.html
latex_engine = 'xelatex'
latex_elements = {
    'fontpkg': r'''
\setmainfont{DejaVu Serif}
\setromanfont{DejaVu Sans}
\setsansfont{DejaVu Sans}
\setmonofont{DejaVu Sans Mono}
'''
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'fedora-faq-ru.tex', 'Неофициальный FAQ по Fedora',
     'EasyCoding Team and contributors', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'fedora-faq-ru', 'Неофициальный FAQ по Fedora',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'fedora-faq-ru', 'Неофициальный FAQ по Fedora',
     author, 'fedora-faq-ru', 'Неофициальный FAQ по Fedora на русском языке.',
     'Miscellaneous'),
]
