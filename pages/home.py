import dash
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

from config.urls_speckle import *

dash.register_page(__name__, path="/")

MODELS_LOADED = 6  # Number of models to load automatically
GRID_SIZE = 2  # Number of cards per row

# LAYOUT COMPONENTS
welcome_modal = html.Div([
    dbc.Modal(
        [
            dbc.ModalHeader(""),
            dbc.ModalBody(
                [
                    html.H2("Speckle Mockup"),
                    html.P("""
                    Welcome to my mockup, a unique platform dedicated to showcasing my fast 
                    parametric models of architectural masterpiece projects. This app is designed 
                    to highlight 
                    the geometric pipelines created completely with grasshopper, focusing on the 
                    general shape, structure and distinctive elements while copying and 
                    understanding some of the most outstanding project.
                     
                    The dash only has 2 layouts. The first one is a grid with the selected 
                    projects and the second one is a modal with the project details, 
                    screenshots and a brief description of the grasshopper workflow."""),
                    # html.Br(),
                    html.P("""                    
                    - The AEC technologies used in the projects are: Grasshopper, Hops, Karamba3d, 
                    Elefront, Speckle, Compute"""),
                    html.P("""
                    - The app was made using: Dash, Python, HTML, CSS, Docker, Github and Azure.
                    """),
                    html.I("""
                    Disclosure: Due the small time available to develop the script, the emphasis 
                    here is not on construction accuracy, but on geometrical workflows of each 
                    model. 
                    Understand the main logic behind the key elements of the project. The Speckle 
                    models are combined to improve loading performance.
                    """
                           ),
                ]
            ),
        ],
        id="modal_welcome",
        size='lg',
        centered=True,
        is_open=True,
    ),
])

header = dbc.NavbarSimple(
    children=[
        dbc.Row([html.H2(
            "Speckle Mockup by Luis Casas", className='app-header-title'),
            # html.P(
            #     "A platform dedicated to showcasing my parametric models of architectural "
            #     "masterpieces"),
        ], justify='center'),

        # Matinee component recommended for future use
        # dmc.Switch(
        #     id="switch",
        #     onLabel="DEV",
        #     offLabel="NOOB",
        #     color="blue",
        #     size="lg",
        #     checked=False
        # ),
    ],
    sticky="top",
    className='app-header justify-content-center',
)

footer = html.Footer([
    html.Div(id='grid-container_sub3', children=[
        html.Div([
            html.Div([
                html.Img(src='/static/icons/life-preserver.svg', className='icon-item-icon'),
                html.H3('Help Center'),
                html.P('Answers to frequently asked account and billing questions.'),
                html.A('Example Link', href='https://www.example.com')
            ], className='footer-item')
        ], id='grid-item-51', className='grid-item'),
        html.Div([
            html.Div([
                html.Img(src='/static/icons/search.svg', className='icon-item-icon'),
                html.H3('Disclosure'),
                html.P('Ask questions and discuss topics with other developers.'),
                html.A('Example Link', href='https://www.example.com')
            ], className='footer-item')
        ], id='grid-item-52', className='grid-item'),
        html.Div([
            html.Div([
                html.Img(src='/static/icons/broadcast.svg', className='icon-item-icon'),
                html.H3('Service Status'),
                html.P('Check the status of the API services.'),
                html.A('Example Link', href='https://www.example.com')
            ], className='footer-item')
        ], id='grid-item-53', className='grid-item'),
    ], className='footer-grid'),
], className='footer-container')

# MODAL COMPONENTS
modal = dbc.Modal(
    [
        dbc.ModalHeader(id="modal-info-title"),
        dbc.ModalBody(id="modal-body"),
    ],
    id="modal",
    size="xl",
    centered=True,
    is_open=False,
    style={'position': 'fixed'}
)


# GRID COMPONENTS
def create_card(param, models_loaded: int):
    # Number of models with autoloading
    if models_loaded < MODELS_LOADED:
        src_manual = param['src']
    else:
        src_manual = ('%').join(param['src'].split('%')[:-1]) + '%2C%22manualLoad%22%3Atrue%7D'

    # Construct the card
    return dbc.Col(
        dbc.Card(
            [
                html.A(
                    html.Iframe(src=src_manual, width="100%", height="100%",
                                style={'-screen': '98vw'}),
                    href="#",
                    id=param['id'],
                    style={'height': '30rem'}
                ),
                dbc.CardBody(
                    [
                        html.H5(param['title'], className="card-title"),
                        dbc.Badge(param.get('badge', ''), color="info"),
                        html.P(param['card_introduction']),
                        dbc.Button("More Info", id=f"more-info-{param['id']}", color="primary",
                                   className="mt-2")
                    ]
                ),
            ],
        ),
    )


rows = []
for i in range(0, len(params), GRID_SIZE):
    row = dbc.Row(
        [create_card(param, i) for param in params[i:i + GRID_SIZE]],
        className="my-4 mx-5"
    )
    rows.append(row)

grid = dbc.Container(rows, fluid=True)

pagination = dmc.Stack(
    dmc.Pagination(total=20, siblings=1, value=10),
    align="center",
    justify="center",
)

# MAIN
layout = html.Div([
    header,
    dcc.Location(id='url', refresh=True),
    welcome_modal,
    header,
    html.Div(style={'height': '3.4rem'}),
    dcc.Loading(
        id="loading",
        type="dot",
        fullscreen=True,
        children=[
            grid,
            modal
        ]),
    footer
])
