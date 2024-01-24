import sphinx_material

# -- Project information

project = 'Mix Master API'
copyright = '2024, Robert Hernes Arnorsson'
author = 'Robert Hernes Arnorsson'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    "sphinx.ext.autodoc",
    "numpydoc",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "nbsphinx",
    "sphinx_markdown_tables",
    "sphinx_copybutton",
    "sphinx_search.extension",
    "myst_parser",
]

extensions.append("sphinx_material")
html_theme_path = sphinx_material.html_theme_path()
html_context = sphinx_material.get_html_context()
html_theme = "sphinx_material"

html_show_sourcelink = False
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

autosummary_generate = True
autoclass_content = "class"

templates_path = ['_templates']

# -- Options for HTML output

html_title = 'Mix Master API Doc'

html_theme = 'sphinx_material'

html_theme_options = {

    'nav_title': 'Mix Master API',

    'base_url': 'https://github.com/RobertArnosson/mixmasterapidoc',

    'color_primary': 'purple',
    'color_accent': 'light-purple',
    'logo_icon': '&#xe88a',

    'html_minify': True,
    'html_prettify': False,
    'css_minify': True,

    'repo_url': 'https://github.com/RobertArnosson/mixmasterapidoc',
    'repo_name': 'Mix Master API Doc',
    'repo_type': 'github',

    'globaltoc_depth': 2,

    'master_doc': False,

    'nav_links': [
        {
            'href': 'index',
            'internal': True,
            'title': 'Home'
        },
        {
            'href': 'api',
            'internal': True,
            'title': 'API'
        },
        {
            'href': 'https://github.com/RobertArnosson/mixmasterapidoc',
            'internal': False,
            'title': 'Buy an API Key',
        },
    ],

    'heroes': {
        'index': 'The documentation for the Mix Master API',
        'customization': 'Configuration options to personalize your site.',
    },
    
    "table_classes": ["plain"],
}

language = 'en'

html_last_updated_fmt = ""

todo_include_todos = True
html_favicon = "images/favicon.ico"

html_use_index = True
html_domain_indices = True

nbsphinx_execute = "always"
nbsphinx_kernel_name = "python3"

# -- Options for EPUB output
epub_show_urls = 'footnote'
