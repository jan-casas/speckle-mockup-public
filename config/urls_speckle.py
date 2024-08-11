from dash import html, dcc

# DEFINE THE PROJECTS
durango = {"src": """
https://app.speckle.systems/projects/219ed1d96a/models/b3f6623259#embed=%7B%22isEnabled%22%3Atrue
%2C%22isTransparent%22%3Atrue%2C%22hideSelectionInfo%22%3Atrue%7D
        """,
           "id": "219ed1d96a",
           "title": "No.mad Arquitectos - Durango",
           # "badge": "badge-primary",
           "card_introduction": """
           The Durango Building, designed by Eduardo Arroyo and No-Mad Arquitectos in 2013, 
           is a contemporary architectural gem in Durango, Spain. The building features a central 
           core that organizes service spaces, surrounded by an outer envelope that connects 
           interior spaces to the landscape. The design's orientation and usage create unique 
           housing types, expanding social spaces. Structural elements include a perforated 
           concrete ring and a triangle geometry, enhancing accessibility and interior permeability.
           """,
           "md": html.Div([
               dcc.Markdown("""
    # Durango Building: Architectural and Engineering Overview

    ## Architectural Perspective
    The Durango Building, designed by Eduardo Arroyo and No-Mad Arquitectos, stands out in 
    contemporary architecture with its unique design approach. The design emphasizes flexibility 
    and sustainability, 
    offering a versatile space that adapts to various uses.

    ## Engineering Perspective
    The Durango Building showcases advanced engineering techniques, particularly in its use of 
    sustainable materials and structural systems. The building features a steel and glass 
    framework that provides both strength and transparency. Advanced engineering methods were 
    employed to optimize the building’s performance, including precise calculations for load 
    distribution and energy efficiency. The integration of cutting-edge technologies ensures 
    durability and adaptability, while minimizing environmental impact.

    ## Constructive Systems
    The construction of the Durango Building involved several sophisticated systems:
    - **Steel Frame Structure**: Provides robust support and allows for expansive glass facades 
    and open interior spaces.
    - **Glass Facade**: Large glass panels enhance natural light and create a seamless connection 
    between the interior and exterior environments.
    - **Sustainable Materials**: Use of eco-friendly materials and construction methods to 
    promote energy efficiency and reduce the building's carbon footprint.
    - **Advanced Engineering Techniques**: Detailed structural analysis and innovative design 
    solutions to ensure performance and resilience.

    ## Conceptual Ideas by Eduardo Arroyo and No-Mad Arquitectos
    Eduardo Arroyo and No-Mad Arquitectos envisioned the Durango Building as a model of modern 
    architecture that balances aesthetic appeal with environmental responsibility. Key conceptual 
    ideas include:
    - **Modern Aesthetics**: The building's design emphasizes clean lines, geometric forms, 
    and a striking visual presence.
    - **Flexibility**: Interiors are designed to be adaptable, accommodating various uses and 
    evolving needs.
    - **Sustainability**: Commitment to using sustainable materials and practices to enhance 
    energy efficiency and minimize environmental impact.
    - **Integration with Environment**: The design integrates seamlessly with its surroundings, 
    creating a cohesive urban presence.

    """),
               html.Img(src="/static/images/durango1.png", className="responsive-img"),
               dcc.Markdown("""
    ## Key Features
    - **Innovative Facade**: Modern materials and geometric forms create a visually striking 
    exterior.
    - **Steel and Glass Framework**: Provides strength and transparency, allowing for expansive 
    interior spaces.
    - **Sustainable Design**: Use of eco-friendly materials and energy-efficient systems.
    - **Adaptable Interiors**: Flexible spaces designed to meet a variety of functional 
    requirements.
    """),
               html.Img(src="/static/images/durango2.jpg", className="responsive-img"),
               dcc.Markdown("""
    The Durango Building exemplifies a successful integration of modern architectural design and 
    advanced engineering. Eduardo Arroyo and No-Mad Arquitectos have created a structure that not 
    only meets functional requirements but also stands as a testament to innovative design and 
    sustainable practices.
    """),
               html.Img(src="/static/images/durango3.jpg", className="responsive-img")
           ])
           }
mediatic = {"src": """
https://app.speckle.systems/projects/35ba1243e5/models/1c34c1b412
#embed=%7B%22isEnabled%22%3Atrue%2C%22isTransparent%22%3Atrue%2C%22hideSelectionInfo%22
%3Atrue%7D
                    """,
            "id": "3125f1b4e5",
            "title": "Cloud 9 - Media TIC",
            # "badge": "badge-primary",
            "card_introduction": """The Media-TIC building, designed by Enric Ruiz-Geli of Cloud 
            9, is a pioneering example of modern architecture and engineering. 
    Known for its innovative use of ETFE cushions, the building achieves exceptional energy 
    efficiency and a striking visual impact. 
    It features a prefabricated concrete structure that allows for precise construction and 
    minimal waste. The design emphasizes 
    sustainability, digital connectivity, and flexibility, creating a dynamic workspace that 
    integrates seamlessly with its urban context.""",
            "md": html.Div([
                dcc.Markdown("""
            # Media-TIC Building: Architectural and Engineering Overview

            ## Architectural Perspective
            The Media-TIC building, designed by Enric Ruiz-Geli of Cloud 9, stands as a landmark 
            in contemporary architecture. The building's facade, characterized by its innovative 
            use of ETFE (Ethylene Tetrafluoroethylene) cushions, provides thermal insulation and 
            regulates light entry, significantly reducing energy consumption. The design 
            emphasizes transparency and fluidity, reflecting the interconnected nature of the 
            digital age. Inside, open-plan interiors foster collaboration and flexibility, 
            key elements for a modern workspace.

            ## Engineering Perspective
            From an engineering perspective, the Media-TIC building incorporates advanced 
            sustainable technologies. The ETFE cushions not only enhance energy efficiency but 
            also contribute to a lightweight structural framework. The building's framework 
            utilizes a prefabricated concrete system for its foundations, facades, floors, 
            and roofs. This system enables precise parameterization of beam sections, automation 
            of joint placements, and accurate element quantification, streamlining construction 
            and minimizing material waste. Additionally, smart systems integrated into the 
            building's design ensure seamless maintenance and adaptability to future 
            technological advancements.

            ## Constructive Systems
            The construction of the Media-TIC building heavily relies on prefabrication and 
            modular systems:
            - **Prefabricated Concrete**: Used in the foundation, structural elements, 
            and facades, allowing for rapid assembly with high precision.
            - **ETFE Cushions**: Energy-efficient and lightweight, these cushions reduce the load 
            on the structure and enable dynamic architectural forms.
            - **Steel Framework**: The primary structure, made of steel, offers flexibility and 
            strength, supporting the innovative facade and large open spaces inside.
            - **Automated Systems**: Automation in the construction process ensures precision in 
            the placement of joints and elements, reducing human error and expediting 
            construction timelines.

            ## Conceptual Ideas by Cloud9 and Enric Ruiz-Geli
            Enric Ruiz-Geli envisioned the Media-TIC building as a model of sustainability, 
            innovation, and digital connectivity. Key concepts include:
            - **Sustainability**: The building embodies environmental responsibility by using 
            advanced materials and systems to minimize energy consumption and carbon footprint.
            - **Innovation**: Incorporating cutting-edge materials like ETFE and smart building 
            technologies showcases the innovative spirit of the digital era.
            - **Digital Connectivity**: The design promotes a connected workspace with open, 
            adaptable interiors that facilitate collaboration and the free flow of information.
            - **Urban Integration**: The building interacts dynamically with its urban 
            environment through its facade and public spaces, creating a dialogue between the 
            structure and the city.

            ## Key Features
            - **Sustainable Design**: ETFE cushions for thermal regulation and light control.
            - **Innovative Structure**: Prefabricated concrete systems for efficient construction.
            - **Smart Technology**: Integration of automated systems for maintenance and 
            adaptability.
            - **Modular Construction**: Prefabricated elements for quick and precise assembly.
            - **Open Plan Interiors**: Flexible spaces designed for collaboration and adaptability.
                """),
                html.Img(src="/static/images/media-tic1.png", className="responsive-img"),
                html.Img(src="/static/images/media-tic2.png", className="responsive-img"),
                html.Figcaption("General view of the Media-TIC building facade and structure"),

                # Detailed Constructive Analysis
                dcc.Markdown("""
            ## Detailed Constructive Analysis
            The Media-TIC building features key structural elements and innovative facade designs:
            - The exterior structure incorporates the ETFE facade and a curtain wall system.
            - The cloud facade releases gas to create a cloud that blocks sunlight, optimizing 
            energy efficiency.
            - Partial beam structures on the upper floors and cantilever slabs shape the living 
            spaces.
            - The building employs three insulation systems against solar incidence, distributed 
            based on system performance and facade orientation. The ETFE and curtain wall act as 
            ventilated walls, while the cloud system blocks light on the north-facing facade.
                """),
                html.Img(src="/static/images/media-tic3.png", className="responsive-img"),
                html.Img(src="/static/images/media-tic4.png", className="responsive-img"),
                html.Figcaption(
                    "Axonométric view of the Media-TIC building facade and structural "),

                # Scripts and Algorithms
                dcc.Markdown("""
            ## Scripts and Algorithms
            Advanced algorithms and components are used to model the building's structure and 
            facade. Python 3 is integrated into the algorithm, enabling real-time data import, 
            Postgres data refresh, and color ramp adjustments, enhancing the accuracy and 
            functionality of the building's data management system (another related project).
                """),
                html.Img(src="/static/images/media-tic6.png", className="responsive-img"),
                html.Img(src="/static/images/media-tic7.png", className="responsive-img"),
                html.Figcaption("Grasshopper scripts for the Media-TIC building general design, "
                                "structure and facade elements."),

            ])
            }
euskotren = {
    "src": """
          https://app.speckle.systems/projects/0e5d383e76/models/4e460a10fa@929d1db715,
          5d1d46a61f@6773a79b88,a1d88e391c@36680e09fb,
          fafbfe7c9f@f1e1909b43#embed=%7B%22isEnabled%22%3Atrue%2C%22isTransparent%22%3Atrue%2C
          %22hideControls%22%3Atrue%2C%22hideSelectionInfo%22%3Atrue%7D
                    """,
    "id": "f4e460a10fa",
    "title": "No.mad Arquitectos - Euskotren",
    # "badge": "badge-primary",
    "card_introduction": """
    The Euskotren proposal project, designed by Eduardo Arroyo from No.Mad Arquitectura, 
    represents a forward-thinking vision for 
    transportation infrastructure in the Basque Country. This project aims to create a landmark 
    that harmoniously integrates with 
    its urban environment while enhancing the efficiency and aesthetics of the transportation 
    hub. The design emphasizes fluidity, 
    movement, and connectivity, with a dynamic structure that mirrors the flow of trains and 
    passengers.
    """,
    "md": html.Div([
        dcc.Markdown("""
    # Euskotren Proposal Project: Architectural and Engineering Overview

    ## Architectural Perspective
    The Euskotren proposal project by Eduardo Arroyo from No.Mad Arquitectura represents a 
    visionary approach to transportation infrastructure 
    in the Basque Country, Spain. The design focuses on creating a landmark that integrates 
    seamlessly with its urban context while providing 
    an efficient and aesthetically pleasing transportation hub. The architecture emphasizes 
    fluidity, movement, and connectivity, with a 
    dynamic form that reflects the flow of trains and passengers.

    ## Engineering Perspective
    From an engineering standpoint, the Euskotren project incorporates advanced structural and 
    transportation technologies. The design 
    features a robust steel and concrete framework that supports large spans and open spaces 
    necessary for transportation facilities. 
    The use of sustainable materials and energy-efficient systems ensures the project's long-term 
    viability and minimal environmental impact. 
    Additionally, the project integrates advanced transportation management systems to optimize 
    the flow of trains and passengers.

    ## Constructive Systems
    The construction of the Euskotren proposal involves several advanced systems:
    - **Steel and Concrete Structure**: Provides the necessary strength and durability for a 
    large-scale transportation hub, allowing 
      for expansive open spaces.
    - **Sustainable Materials**: Use of recycled and locally sourced materials to reduce 
    environmental impact.
    - **Energy-Efficient Systems**: Incorporation of advanced HVAC, lighting, and energy 
    management systems to minimize energy consumption.
    - **Modular Construction**: Use of prefabricated elements to streamline construction, 
    reduce waste, and ensure high precision.
"""),
        html.Img(src="/static/images/euskotren1.jpg", className="responsive-img"),
        html.Figcaption("Main systems of the Euskotren proposal project"),

        dcc.Markdown("""
    ## Conceptual Ideas by Eduardo Arroyo
    Eduardo Arroyo’s vision for the Euskotren project is to create a transportation hub that is 
    not only functional and efficient but also 
    a symbol of modernity and sustainability. Key conceptual ideas include:
    - **Fluidity and Movement**: Reflecting the dynamic nature of transportation with a flowing, 
    organic design.
    - **Urban Integration**: Designing a structure that complements and enhances its urban 
    surroundings.
    - **Sustainability**: Incorporating green building practices and energy-efficient technologies.
    - **Passenger Experience**: Prioritizing the comfort and convenience of passengers with 
    intuitive navigation and pleasant waiting areas.

    """),
        # Axonometric cut
        html.Img(src="/static/images/euskotren2.jpeg", className="responsive-img"),
        html.Img(src="/static/images/euskotren3.jpeg", className="responsive-img"),
        html.Figcaption("Axonometric cut of the main structural systems of the Euskotren proposal "
                        "project"),

        html.Img(src="/static/images/euskotren4.png", className="responsive-img"),
        html.Figcaption(
            "Grasshopper scripts for the Euskotren proposal project design and structural "
            "elements."),
    ]),
}
pitch = {
    "src": """
    https://app.speckle.systems/projects/e7fde27118/models/fa0380f058#embed=%7B%22isEnabled%22
    %3Atrue%2C%22isTransparent%22%3Atrue%2C%22hideSelectionInfo%22%3Atrue%7D
    """,
    "id": "hte7fde27118",
    "title": "Pitch Arquitectos - Gonsi Sócrates Viladecans",
    # "badge": "badge-primary",
    "card_introduction": """
        El Edificio Gonsi Sócrates, designed by Pitch Arquitectos, is a state-of-the-art office 
        building in Viladecans, Spain, exemplifying modern architecture and sustainability. The 
        building features a sleek, contemporary facade with extensive glass surfaces that enhance 
        natural light and visual impact. Inside, the flexible steel frame structure and 
        high-performance glazing system ensure adaptability and energy efficiency. This design 
        integrates renewable energy sources, reflecting a commitment to environmental 
        responsibility and user comfort.
    """,
    "md": html.Div([
        dcc.Markdown("""
    # El Edificio Gonsi Sócrates Viladecans: Architectural and Engineering Overview

    ## Architectural Perspective
    El Edificio Gonsi Sócrates, designed by Pitch Arquitectos, is a cutting-edge office building 
    located in Viladecans, Spain. 
    This contemporary structure is known for its innovative design and sustainable features. The 
    architecture emphasizes 
    functionality, flexibility, and a modern aesthetic that aligns with the needs of contemporary 
    businesses. The building's 
    facade, characterized by its sleek lines and expansive glass surfaces, creates a dynamic 
    visual presence and allows for 
    ample natural light within.

    ## Engineering Perspective
    From an engineering standpoint, El Edificio Gonsi Sócrates incorporates advanced construction 
    techniques and sustainable 
    technologies. The building features a steel frame structure that supports large open spaces, 
    providing flexibility in the 
    interior layout. The facade includes a high-performance glazing system that enhances energy 
    efficiency and occupant comfort. 
    Additionally, the building integrates renewable energy sources, such as photovoltaic panels, 
    to reduce its environmental impact 
    and operational costs.

    ## Constructive Systems
    The construction of El Edificio Gonsi Sócrates involved several advanced systems:
    - **Steel Frame Structure**: Provides the primary support and allows for large, open interior 
    spaces that can be easily adapted.
    - **High-Performance Glazing**: Enhances energy efficiency by reducing heat gain and loss, 
    while maximizing natural light.
    - **Renewable Energy Integration**: Photovoltaic panels and other renewable energy systems 
    reduce the building's carbon footprint.
    - **Prefabricated Components**: Use of prefabricated elements ensured precision, 
    reduced construction time, and minimized on-site labor.

    ## Conceptual Ideas by Pitch Arquitectos
    Pitch Arquitectos’ vision for El Edificio Gonsi Sócrates was to create a workspace that is 
    not only functional and modern but also 
    environmentally responsible. Key conceptual ideas include:
    - **Sustainability**: Incorporating renewable energy sources and high-performance materials 
    to minimize environmental impact.
    - **Flexibility and Adaptability**: Designing open interior spaces that can easily be 
    reconfigured to meet changing needs.
    - **Modern Aesthetic**: Emphasizing clean lines, transparency, and a sleek, contemporary 
    appearance.
    - **User Comfort**: Prioritizing natural light, energy efficiency, and overall occupant 
    well-being.

    """),
        html.Img(src="/static/images/gonsi1.png", className="responsive-img"),
        dcc.Markdown("""
    ## Key Features
    - **Steel Frame Structure**: Provides flexibility and strength, allowing for adaptable 
    interior spaces.
    - **High-Performance Glazing**: Improves energy efficiency and occupant comfort.
    - **Renewable Energy Systems**: Integration of photovoltaic panels to reduce carbon footprint 
    and operational costs.
    - **Modern Design**: Sleek lines and expansive glass surfaces reflecting contemporary 
    architectural trends.
    """),
        html.Img(src="/static/images/gonsi2.png", className="responsive-img"),
        dcc.Markdown("""
    El Edificio Gonsi Sócrates stands as a testament to Pitch Arquitectos' commitment to 
    sustainability, modern design, and 
    flexible, user-centric spaces. The building exemplifies how contemporary architecture can 
    create functional, beautiful, 
    and environmentally responsible work environments.
    """),
        html.Img(src="/static/images/gonsi3.png", className="responsive-img")
    ]),

}
absolute = {
    "src": """
   https://app.speckle.systems/projects/12577d7c6e/models/08a3f5ad58#embed=%7B%22isEnabled%22
   %3Atrue%2C%22isTransparent%22%3Atrue%2C%22hideSelectionInfo%22%3Atrue%7D
    """,
    "id": "089f8d1d96a",
    "title": "Mad Architects - Absolute Towers",
    # "badge": "badge-primary",
    "card_introduction": """
    The Absolute Towers, designed by MAD Architects, are iconic residential skyscrapers in 
    Mississauga, Ontario, renowned for their distinctive twisting forms. Nicknamed the "Marilyn 
    Monroe Towers," these structures defy conventional high-rise design with their fluid, 
    organic curves. The towers feature continuous balconies that enhance both their aesthetic 
    appeal and structural stability. This landmark project showcases advanced engineering and 
    innovative design, creating a dynamic visual impact on the city skyline.
    """,
    "md": html.Div([
        dcc.Markdown("""
    # Absolute Towers: Architectural and Engineering Overview

    ## Architectural Perspective
    The Absolute Towers, designed by MAD Architects, are a striking pair of residential 
    skyscrapers located in Mississauga, Ontario, Canada. Nicknamed the "Marilyn Monroe Towers" 
    due to their sensuous curves, the buildings stand out for their organic, twisting forms. This 
    design breaks away from the conventional boxy high-rise structures, creating a dynamic and 
    fluid visual effect that changes depending on the angle from which they are viewed. The 
    continuous balconies that wrap around each floor not only<_ provide expansive views but also 
    enhance the building's sculptural quality.

    ## Engineering Perspective
    Engineering the Absolute Towers required innovative solutions to achieve their distinctive 
    twisting shape. The structural system is a combination of a reinforced concrete core and a 
    perimeter of columns that support the slabs. Each floor is uniquely shaped and rotated 
    incrementally from the one below, requiring precise engineering and construction techniques. 
    Advanced modeling software was used to ensure structural integrity and to plan the complex 
    geometry. Wind tunnel testing was also critical to ensure the towers' stability and comfort 
    for residents.

    The project incorporates three main structural layers: 
    - **Horizontal Structural Systems (Slabs)**: These provide the primary floor support, 
    with each slab carefully designed to accommodate the twisting form and varying load 
    distribution.
    - **Vertical Structural Systems**: These include the elevator core, columns, and walls, 
    which provide vertical support and stability to the structure. The elevator core is central 
    to the building's stability, while the columns and walls adjust to the twisting geometry.
    - **Façade**: Comprising the curtain wall and railings, the façade not only enhances the 
    towers' aesthetic appeal but also contributes to the overall structural integrity.

    ## Constructive Systems
    The construction of the Absolute Towers involved several advanced systems:
    - **Reinforced Concrete Core**: Provides the primary structural support and houses elevators 
    and utilities.
    - **Perimeter Columns**: Support the twisting floor slabs and allow for the building's 
    signature curves.
    - **Rotating Floor Plates**: Each floor plate is slightly rotated from the one below, 
    requiring precise alignment and formwork.
    - **Continuous Balconies**: These wrap around each floor, not only enhancing the aesthetic 
    but also providing structural stability and acting as horizontal bracing.
    - **Cladding and Glazing**: High-performance glazing and cladding materials ensure energy 
    efficiency and complement the towers' sleek appearance.
"""),

        html.Img(src="/static/images/absolute-towers1.png",
                 className="responsive-img"),
        html.Figcaption(
            "Main layers of study for the Absolute Towers, including the structural systems, "
            "facade systems and slab/core structural analysis"),

        html.Img(src="/static/images/absolute-towers2.png", className="responsive-img"),
        html.Figcaption(
            "Key structural elements of the tower and its analysis"),

        dcc.Markdown("""
    A structural simulation was conducted to account for the supports at each floor and the 
    deformation of the slab under residential loads, ensuring the towers' long-term stability and 
    comfort for residents.

    ## Conceptual Ideas by MAD Architects
    MAD Architects' vision for the Absolute Towers was to create buildings that are more than 
    just functional residential spaces, but also landmarks that redefine the city's skyline. Key 
    conceptual ideas include:
    - **Organic Form**: Inspired by natural forms, the design aims to create a sense of movement 
    and fluidity.
    - **Human-Centric Design**: The continuous balconies and panoramic views are intended to 
    connect residents more closely with their surroundings.
    - **Iconic Silhouette**: The towers' unique shapes make them instantly recognizable and a 
    symbol of modern architectural innovation.
    - **Integration with Environment**: The design seeks to harmonize with the natural and urban 
    landscape, creating a dialogue between the built environment and its context.
        """),

        dcc.Markdown("""
    ## Key Features
    - **Distinctive Design**: Twisting forms that create a dynamic visual impact.
    - **Advanced Engineering**: Innovative structural solutions to achieve the complex geometry.
    - **Sustainable Materials**: Use of high-performance glazing and energy-efficient systems.
    - **Panoramic Views**: Continuous balconies providing expansive views from every floor.
        """),

        html.Img(src="/static/images/absolute-towers3.png", className="responsive-img"),
        html.Figcaption("Revit model transferred using Rhino Inside Revit (2020)"),

        html.Img(src="/static/images/absolute-towers4.png", className="responsive-img"),
        html.Figcaption(
            "Grasshopper scripts for the Absolute Towers design, structural elements and simple "
            "analysis"),
    ])

}
les_corts = {
    "src": """
    https://app.speckle.systems/projects/f18e63802f/models/26fa094152#embed=%7B%22isEnabled%22
    %3Atrue%2C%22isTransparent%22%3Atrue%2C%22hideSelectionInfo%22%3Atrue%7D
    """,
    "id": "vfb219ed1d96a",
    "title": "Eduardo Torroja - Tribuna Les Corts",
    # "badge": "badge-primary",
    "card_introduction": """
    La Tribuna de Les Corts, designed by Eduardo Torroja, is a landmark of early 20th-century 
    architecture located in Barcelona. Completed in 1929, this grandstand is celebrated for its 
    modernist design and innovative use of reinforced concrete. Torroja's pioneering techniques, 
    including cantilevered roofs and thin-shell construction, offer both aesthetic appeal and 
    functionality. The structure exemplifies how cutting-edge engineering and modernist 
    principles can create a striking and practical sports venue.
    """,
    "md": html.Div([
        dcc.Markdown("""
    # La Tribuna de Les Corts: Architectural and Engineering Overview

    ## Architectural Perspective
    La Tribuna de Les Corts, designed by Eduardo Torroja, is an exemplary piece of early 
    20th-century architecture located in Barcelona, Spain. 
    Completed in 1929 for the Les Corts stadium (the former home of FC Barcelona), this grandstand 
    is notable for its sleek, modernist design and innovative use of materials. Torroja’s design 
    prioritizes functionality and aesthetics, creating a structure that offers excellent views for 
    spectators while embodying the principles of modern architecture.

    ## Engineering Perspective
    From an engineering perspective, La Tribuna de Les Corts is a landmark project showcasing 
    Torra’s pioneering use of reinforced concrete. The grandstand features a cantilevered roof 
    that spans large distances without the need for supporting columns, providing unobstructed 
    views. This achievement was made possible through the use of thin-shell concrete construction, 
    a technique that Torroja mastered and popularized. The structural design ensures stability and 
    durability while using minimal material, reflecting Torroja’s commitment to efficiency and 
    innovation.

    ## Constructive Systems
    The construction of La Tribuna de Les Corts involved several advanced systems:
    - **Reinforced Concrete Cantilevers**: The roof is supported by reinforced concrete 
    cantilevers, which extend outward to provide cover without obstructing views.
    - **Thin-Shell Construction**: The use of thin-shell concrete techniques allows for a 
    lightweight yet strong structure, reducing material usage and construction costs.
    - **Modular Elements**: The design incorporates modular elements that simplify construction 
    and ensure uniformity.
    - **Precision Formwork**: Custom formwork was used to create the precise shapes needed for 
    the thin-shell concrete structures, ensuring both aesthetic and structural integrity.
        """),
        html.Img(src="/static/images/tribuna-les-corts1.png", className="responsive-img"),
        html.Figcaption(
            "Main structural systems of the Les Corts grandstand, including the cantilevered roof "
            "and prefabricated elements."),

        dcc.Markdown("""
    ## Conceptual Ideas by Eduardo Torroja
    Eduardo Torroja’s vision for La Tribuna de Les Corts was to create a grandstand that combines 
    modern aesthetics with innovative engineering. Key conceptual ideas include:
    - **Modernist Design**: Emphasizing clean lines, functional forms, and the honest expression 
    of materials.
    - **Structural Innovation**: Using cutting-edge techniques in reinforced concrete to achieve 
    large spans and cantilevers.
    - **Spectator Experience**: Prioritizing the comfort and viewing experience of spectators, 
    with unobstructed sightlines and protection from the elements.
    - **Material Efficiency**: Minimizing material use through innovative design, reflecting 
    Torra’s principles of efficiency and sustainability.
        """),

        dcc.Markdown("""
    ## Key Features
    - **Cantilevered Roof**: Provides unobstructed views and protection from the elements.
    - **Innovative Use of Concrete**: Thin-shell construction and reinforced concrete cantilevers 
    showcase advanced engineering techniques.
    - **Modernist Aesthetic**: Clean lines and functional design embody the principles of modern 
    architecture.
    - **Historical Significance**: A pioneering example of early 20th-century sports architecture 
    and engineering.
        """),

        html.Img(src="/static/images/tribuna-les-corts3.png", className="responsive-img"),
        html.Figcaption(
            "Grasshopper scripts for the Les Corts grandstand design and structural elements."),

    ])

}
zarzuela = {
    "src": """
    https://app.speckle.systems/projects/833e480ef0/models/2e71dc8ee7#embed=%7B%22isEnabled%22
    %3Atrue%2C%22isTransparent%22%3Atrue%2C%22hideSelectionInfo%22%3Atrue%7D
    """,
    "id": "214f8d1d96a",
    "title": "Eduardo Torroja - Hipódromo Zarzuela",
    # "badge": "badge-primary",
    "card_introduction": """
    El Hipódromo de la Zarzuela, designed by Eduardo Torroja and completed in 1941, stands as a 
    pinnacle of modernist architecture in Madrid. Known for its elegant undulating roof, 
    the grandstand combines aesthetic beauty with innovative engineering. The structure features 
    thin-shell, cantilevered concrete shells that provide unobstructed views and exemplify 
    Torroja’s mastery of reinforced concrete. This landmark not only enhances the spectator 
    experience but also represents a significant achievement in architectural and engineering 
    design.
    """,
    "md": html.Div([
        dcc.Markdown("""
    # El Hipódromo de la Zarzuela: Architectural and Engineering Overview

    ## Architectural Perspective
    El Hipódromo de la Zarzuela, designed by Eduardo Torroja, is a masterpiece of modernist 
    architecture located in Madrid, Spain. 
    Completed in 1941, the building is renowned for its elegant and functional design that 
    seamlessly integrates form and function. 
    The grandstand roof, with its distinctive undulating curves, is both an aesthetic and 
    structural marvel, symbolizing the dynamism 
    and movement of horse racing. The architectural design focuses on providing unobstructed 
    views for spectators, creating a 
    comfortable and immersive experience.

    ## Engineering Perspective
    From an engineering standpoint, the grandstand roof of El Hipódromo de la Zarzuela is a 
    pioneering achievement. Torroja employed 
    innovative use of reinforced concrete to create thin-shell, cantilevered structures that 
    cover large spans without internal supports. 
    The roof is composed of three large hyperbolic paraboloid shells, each extending over 12 
    meters, which was an extraordinary 
    engineering feat at the time. This design minimizes material use while maximizing structural 
    efficiency and aesthetic impact.

    ## Structural Systems Overview
    The construction of El Hipódromo de la Zarzuela involved several advanced systems:
    - **Reinforced Concrete Shells**: The hyperbolic paraboloid shells are made of thin 
    reinforced concrete, showcasing the material's 
      versatility and strength.
    - **Cantilevered Structure**: The grandstand roof is cantilevered, providing clear sightlines 
    and unobstructed views for spectators.
    - **Modular Design**: The use of repeated modular elements in the roof structure allows for 
    uniformity and ease of construction.
    - **Lightweight Formwork**: Innovative formwork techniques were used to shape the complex 
    curves of the concrete shells, ensuring 
      precision and structural integrity.

    The two diagrams illustrate the main structural systems, including the roofs, stands, vertical 
    structures, and foundations. In addition, the beam diagrams show the compression and tension 
    stresses of each of its members, as well as the force flows in the case of the sheets.
        """),
        html.Img(src="/static/images/hipodromo1.png", className="responsive-img"),
        html.Figcaption("Main structural systems of the Hipódromo de la Zarzuela"),

        dcc.Markdown("""
    ## Conceptual Ideas by Eduardo Torroja
    Eduardo Torroja's vision for El Hipódromo de la Zarzuela was to create a structure that 
    combines beauty, functionality, and 
    structural innovation. Key conceptual ideas include:
    - **Structural Artistry**: The use of hyperbolic paraboloid shells demonstrates how 
    engineering can create visually stunning forms.
    - **Efficiency and Economy**: The design maximizes the efficiency of materials, minimizing 
    waste and construction costs.
    - **Spectator Experience**: The grandstand design prioritizes the comfort and viewing 
    experience of spectators, with unobstructed 
      views and protection from the elements.
    - **Integration with Environment**: The design harmonizes with the surrounding landscape, 
    creating a sense of place and enhancing 
      the overall experience of the venue.
        """),

        dcc.Markdown("""
    ### Advanced Structural Analysis
    The shapes have been obtained using parametric methods, finite element optimization, 
    and form finding. These methods allow for the exploration and calculation of different options, 
    showing the main stress lines, moments, and normal stresses on the sheets.
        """),

        html.Img(src="/static/images/hipodromo3.png", className="responsive-img"),
        html.Figcaption(
            "Key structural analysis: stress lines, main moments, normal stresses, and deflection"),

        dcc.Markdown("""
    ## Key Features
    - **Innovative Roof Design**: Hyperbolic paraboloid shells that are both aesthetically 
    pleasing and structurally efficient.
    - **Clear Sightlines**: Cantilevered structure providing unobstructed views for spectators.
    - **Material Efficiency**: Use of reinforced concrete to achieve large spans with minimal 
    material.
    - **Historical Significance**: A pioneering example of modernist architecture and engineering 
    from the early 20th century.
        """),

        html.Img(src="/static/images/hipodromo2.png", className="responsive-img"),
        html.Figcaption("Grasshopper script for the Hipódromo de la Zarzuela"),
    ])

}
somisa = {
    "src": """
    https://app.speckle.systems/projects/166220d6a4/models/5da6be86ea#embed=%7B%22isEnabled%22
    %3Atrue%2C%22isTransparent%22%3Atrue%2C%22hideSelectionInfo%22%3Atrue%7D
    """,
    "id": "u65eh220d6a4",
    "title": "Mario Roberto - Edificio Somisa",
    # "badge": "badge-primary",
    "card_introduction": """
    El Edificio SOMISA, designed by Mario Roberto Álvarez and completed in 1969, exemplifies 
    modernist architecture in Buenos Aires. Originally built for the steel company SOMISA, 
    the building features a steel frame and glass facade that highlight its industrial strength 
    and modernist ideals. The design focuses on functional, open floor plans and a transparent 
    aesthetic, reflecting the principles of mid-20th-century architecture. With its use of 
    prefabricated steel and glass, the Edificio SOMISA stands as a significant example of 
    architectural innovation and efficiency.
    """,
    "md": html.Div([
        dcc.Markdown("""
        # Edificio SOMISA: Architectural and Engineering Overview

        ## Architectural Perspective
        The Edificio SOMISA, designed by Argentine architect Mario Roberto Álvarez, 
        is a significant example of modernist architecture in Buenos Aires, Argentina. 
        Completed in 1969, this office building was originally constructed for the state-owned 
        steel company SOMISA (Sociedad Mixta Siderúrgica Argentina). 
        The building is renowned for its functional design, clean lines, and extensive use of 
        steel, reflecting the industrial strength and modernist 
        ideals of the mid-20th century. The design emphasizes simplicity, transparency, 
        and a strong connection between form and function.

        ## Engineering Perspective
        From an engineering perspective, the Edificio SOMISA showcases advanced techniques in 
        steel construction. The building features a 
        steel frame structure that allows for open floor plans and flexibility in interior 
        layouts. The use of prefabricated steel components 
        facilitated rapid construction and provided a high degree of precision and structural 
        integrity. The facade is characterized by 
        large glass panels, providing ample natural light and a sense of openness. The innovative 
        use of steel and glass not only 
        highlights the building's modernist aesthetic but also ensures durability and 
        sustainability.

        ## Constructive Systems
        The construction of Edificio SOMISA involved several advanced systems:
        - **Steel Frame Structure**: The primary structural system is composed of prefabricated 
        steel components, allowing for open, 
          column-free interior spaces and flexibility in use.
        - **Glass Curtain Wall**: The facade features a glass curtain wall system, providing 
        natural light and reducing the need for artificial lighting.
        - **Prefabrication**: Extensive use of prefabricated elements ensured precision, 
        reduced construction time, and minimized on-site labor.
        - **Modular Design**: The building's modular design allowed for efficient construction 
        and future adaptability.

        ## Conceptual Ideas by Mario Roberto Álvarez
        Mario Roberto Álvarez’s vision for the Edificio SOMISA was to create a modern office 
        building that embodies the principles of 
        transparency, efficiency, and industrial prowess. Key conceptual ideas include:
        - **Modernist Aesthetic**: Emphasizing clean lines, functional forms, and the honest 
        expression of materials.
        - **Industrial Symbolism**: Using steel as the primary material to symbolize industrial 
        strength and progress.
        - **Transparency and Light**: Designing a facade that maximizes natural light and creates 
        a sense of openness.
        - **Flexibility and Efficiency**: Creating open, adaptable interior spaces that can be 
        easily reconfigured to meet changing needs.

        """),
        html.Img(src="/static/images/somisa1.png", className="responsive-img"),
        dcc.Markdown("""
        ## Key Features
        - **Steel Construction**: Extensive use of prefabricated steel components for the primary 
        structure.
        - **Glass Curtain Wall**: Large glass panels providing natural light and a modern aesthetic.
        - **Open Floor Plans**: Flexible interior spaces designed for adaptability.
        - **Modernist Design**: Clean lines and functional forms reflecting mid-20th-century 
        modernist ideals.
        """),
        html.Img(src="/static/images/somisa2.png", className="responsive-img"),
        dcc.Markdown("""
        The Edificio SOMISA remains a landmark of modernist architecture and engineering in 
        Buenos Aires. Mario Roberto Álvarez's innovative 
        use of steel and glass, combined with his commitment to modernist principles, created a 
        building that is both functional and 
        aesthetically striking. The project stands as a testament to the potential of industrial 
        materials in creating enduring and 
        adaptable architectural works.
        """),
        html.Img(src="/static/images/somisa3.png", className="responsive-img")
    ]),
}
castelar = {
    "src": """
    https://app.speckle.systems/projects/219ed1d96a/models/all#embed=%7B%22isEnabled%22%3Atrue
    %2C%22isTransparent%22%3Atrue%2C%22hideControls%22%3Atrue%2C%22hideSelectionInfo%22%3Atrue%7D
    """,
    "id": "alkjsf8d1d96a",
    "title": "Rafael de La-Hoz - Edificio Castelar",
    # "badge": "badge-primary",
    "card_introduction": """
    Edificio Castelar, designed by Rafael de La-Hoz and completed in 1986, is a standout modern 
    office building in Madrid. Known for its sleek design and extensive use of glass, 
    it emphasizes transparency and integration with its urban environment. The building features 
    advanced engineering solutions, including a double skin facade for enhanced energy efficiency 
    and a steel frame structure for flexible interior spaces. Edificio Castelar represents a 
    fusion of aesthetic appeal, functional design, and sustainability in contemporary architecture.

    """,
    "md": html.Div([
        dcc.Markdown("""
    # Edificio Castelar: Architectural and Engineering Overview

    ## Architectural Perspective
    Edificio Castelar, designed by the renowned Spanish architect Rafael de La-Hoz, is a modern 
    office building located in Madrid, Spain. 
    Completed in 1986, the building is celebrated for its sleek, contemporary design and its 
    integration into the urban fabric of the city. 
    The architecture emphasizes transparency, lightness, and a harmonious relationship with its 
    surroundings. The building’s facade features 
    expansive glass surfaces, providing a sense of openness and connecting the interior spaces 
    with the external environment.

    ## Engineering Perspective
    From an engineering perspective, Edificio Castelar incorporates advanced structural and 
    environmental technologies. The building's 
    steel and glass construction ensures both strength and flexibility, allowing for large open 
    spaces within. The facade includes a 
    double skin system, which improves thermal insulation and energy efficiency. The design also 
    incorporates sustainable technologies 
    such as energy-efficient HVAC systems and advanced building management systems to reduce 
    environmental impact and operational costs.

    ## Constructive Systems
    The construction of Edificio Castelar involved several advanced systems:
    - **Steel Frame Structure**: Provides the primary support and allows for large, open interior 
    spaces without the need for numerous 
      internal columns.
    - **Double Skin Facade**: Enhances thermal performance by creating an air buffer between the 
    two layers of glass, reducing heat 
      gain in the summer and heat loss in the winter.
    - **Sustainable Technologies**: Incorporates energy-efficient HVAC systems, low-emissivity 
    glass, and advanced building management 
      systems to optimize energy use.
    - **Modular Components**: Use of prefabricated elements ensured high precision, 
    reduced construction time, and minimized on-site labor.

    ## Conceptual Ideas by Rafael de La-Hoz
    Rafael de La-Hoz’s vision for Edificio Castelar was to create a building that is not only 
    functional and aesthetically pleasing but 
    also environmentally responsible. Key conceptual ideas include:
    - **Transparency and Lightness**: The extensive use of glass creates a sense of openness and 
    connection with the city.
    - **Sustainability**: Incorporating advanced technologies to reduce the building’s 
    environmental footprint and enhance energy efficiency.
    - **Urban Integration**: Designing a building that harmonizes with its urban context, 
    contributing positively to the cityscape.
    - **Flexibility and Functionality**: Creating adaptable interior spaces that can meet the 
    evolving needs of its occupants.

    """),
        html.Img(src="/static/images/castelar1.png", className="responsive-img"),
        dcc.Markdown("""
    ## Key Features
    - **Double Skin Facade**: Improves energy efficiency and provides better thermal comfort.
    - **Steel and Glass Construction**: Combines strength and flexibility with a modern aesthetic.
    - **Sustainable Design**: Incorporates energy-efficient systems and materials to reduce 
    environmental impact.
    - **Contemporary Aesthetic**: Clean lines, transparency, and lightness reflecting modern 
    architectural principles.
    """),
        html.Img(src="/static/images/castelar2.png", className="responsive-img"),
        dcc.Markdown("""
    Edificio Castelar exemplifies Rafael de La-Hoz’s ability to blend modern architectural design 
    with advanced engineering and 
    sustainable practices. The building stands as a model of how contemporary architecture can 
    create functional, beautiful, and 
    environmentally responsible urban spaces.
    """),
        html.Img(src="/static/images/castelar3.png", className="responsive-img")
    ]),

}
shanghai = {
    "src": """
    https://app.speckle.systems/projects/adc12c2feb/models/fe218cb1e3#embed=%7B%22isEnabled%22
    %3Atrue%2C%22isTransparent%22%3Atrue%2C%22hideSelectionInfo%22%3Atrue%7D
    """,
    "id": "978s8d1d96a",
    "title": "Gensler - Shanghai Tower",
    # "badge": "badge-primary",
    "card_introduction": """
    The Shanghai Tower, completed in 2015, is a marvel of modern engineering and design. 
    Standing at 632 meters, this supertall skyscraper is the second-tallest building in the world 
    and a symbol of Shanghai's rapid growth and innovation. The tower's twisting form and 
    double-skin facade are not only visually striking but also serve functional purposes, 
    enhancing energy efficiency and structural stability. The Shanghai Tower represents a 
    fusion of cutting-edge technology, sustainable practices, and architectural excellence.
    """,
    "md": html.Div([
        dcc.Markdown("""
    # Shanghai Tower: Architectural and Engineering Overview

    ## Architectural Perspective
    The Shanghai Tower, designed by the architectural firm Gensler, is a landmark in contemporary 
    skyscraper design and engineering. Completed in 2015, it stands as the tallest building in 
    China 
    and the second tallest in the world, reaching a height of 632 meters (2,073 feet). Located in 
    Shanghai's Lujiazui area, this iconic structure features a twisting cylindrical design that 
    reduces wind load and enhances structural stability. The tower's sleek glass façade creates a 
    striking visual impact while optimizing energy efficiency and natural light.

    ## Engineering Perspective
    From an engineering perspective, the Shanghai Tower showcases advanced structural and 
    environmental technologies. The building employs a unique structural system with a central core 
    and tapered cylindrical layers that provide stability and flexibility. The double-layered glass 
    façade improves thermal performance, while the use of sustainable technologies such as 
    energy-efficient 
    HVAC systems contributes to its LEED Platinum certification. The tower also integrates 
    innovative 
    wind-turbine technology to generate renewable energy.

    ## Constructive Systems
    The construction of Shanghai Tower involved several advanced systems:
    - **Cylindrical Structure**: A twisting, cylindrical design that reduces wind resistance and 
    enhances 
      structural stability.
    - **Double-Layered Glass Facade**: Provides thermal insulation and maximizes natural light 
    while reducing 
      energy consumption.
    - **Sustainable Technologies**: Includes energy-efficient HVAC systems, wind turbines, 
    and rainwater 
      harvesting to support the tower’s LEED Platinum status.
    - **Modular Construction**: Use of prefabricated components allowed for high precision and 
    efficiency in 
      construction.

    ## Conceptual Ideas by Gensler
    Gensler's vision for the Shanghai Tower was to create a skyscraper that embodies modern 
    architectural 
    and engineering principles while addressing environmental and urban challenges. Key 
    conceptual ideas include:
    - **Iconic Design**: A twisting form that symbolizes progress and innovation while mitigating 
    wind load.
    - **Sustainability**: Emphasizing energy efficiency and incorporating renewable energy 
    sources to reduce 
      the building’s environmental impact.
    - **Urban Integration**: Designed to harmonize with the cityscape and contribute to the urban 
    fabric of 
      Shanghai.
    - **Vertical City**: The building integrates office spaces, retail areas, and public 
    amenities within a single 
      vertical structure, enhancing functionality and accessibility.

    """),
        html.Img(src="/static/images/shanghai-tower1.png", className="responsive-img"),
        dcc.Markdown("""
    ## Key Features
    - **Twisting Cylindrical Design**: Reduces wind load and provides structural stability.
    - **Double-Layered Glass Facade**: Enhances thermal insulation and energy efficiency.
    - **Sustainable Technologies**: Incorporates wind turbines and energy-efficient systems.
    - **Vertical City Concept**: Integrates multiple functions within a single structure.
    - **Iconic Architecture**: Represents modernity and innovation in skyscraper design.
    """),
        html.Img(src="/static/images/shanghai-tower2.png", className="responsive-img"),
        dcc.Markdown("""
    The Shanghai Tower exemplifies Gensler's innovative approach to skyscraper design and 
    sustainability. 
    Its striking design and advanced engineering make it a prominent landmark in Shanghai, 
    showcasing 
    the potential of modern architecture to address both functional and environmental challenges.
    """),
        html.Img(src="/static/images/shanghai-tower3.png", className="responsive-img")
    ])
}
cherry = {
    "src": """
    https://app.speckle.systems/projects/219ed1d96a/models/all#embed=%7B%22isEnabled%22%3Atrue
    %2C%22isTransparent%22%3Atrue%2C%22hideControls%22%3Atrue%2C%22hideSelectionInfo%22%3Atrue%7D
    """,
    "id": "alkjsf8d1d96a",
    "title": "Cherry Blossom Pavilion",
    # "badge": "badge-primary",
    "card_introduction": """
    The Cherry Blossom Pavilion, designed by Cero9 Arquitectos, is a striking pavilion located
    in the picturesque Jerte Valley, Spain. Completed in 2021, this pavilion is a tribute to the
    beauty of the cherry blossoms that bloom in the valley. Its design features a fluid, organic
    form that mimics the delicate petals of the cherry blossoms. The pavilion’s exterior is covered
    with a perforated metal skin that creates a dynamic interplay of light and shadow, reflecting
    the changing light conditions throughout the day and adding a sense of ephemeral beauty to the
    structure.
    """,
    "md": html.Div([
        dcc.Markdown("""
    # Cherry Blossom Pavilion: Architectural and Engineering Overview

    ## Architectural Perspective
    The Cherry Blossom Pavilion, designed by Cero9 Arquitectos, led by Cristina and Efren, 
    is a striking 
    pavilion located in the picturesque Jerte Valley, Spain. Completed in 2021, this pavilion is 
    a tribute 
    to the beauty of the cherry blossoms that bloom in the valley. Its design features a fluid, 
    organic form 
    that mimics the delicate petals of the cherry blossoms. The pavilion’s exterior is covered 
    with a 
    perforated metal skin that creates a dynamic interplay of light and shadow, reflecting the 
    changing 
    light conditions throughout the day and adding a sense of ephemeral beauty to the structure.

    ## Engineering Perspective
    From an engineering standpoint, the Cherry Blossom Pavilion is notable for its innovative use 
    of materials 
    and structural techniques. The pavilion's unique shape is achieved through a combination of 
    advanced 
    digital modeling and precision fabrication. The structure employs a lightweight steel 
    framework that 
    supports the intricate metal skin while allowing for expansive open spaces inside. The 
    pavilion also 
    features sustainable design elements, including natural ventilation and rainwater collection 
    systems, 
    enhancing its environmental performance and integration with the surrounding landscape.

    ## Constructive Systems
    The construction of the Cherry Blossom Pavilion involved several advanced systems:
    - **Lightweight Steel Framework**: Provides structural support for the pavilion’s complex 
    geometry while 
      minimizing material use.
    - **Perforated Metal Skin**: Creates a dynamic play of light and shadow, inspired by the 
    petals of cherry 
      blossoms, and contributes to the pavilion's aesthetic and functional qualities.
    - **Digital Modeling and Precision Fabrication**: Utilizes advanced modeling techniques to 
    ensure precision 
      in the construction of the pavilion’s intricate form.
    - **Sustainable Features**: Includes natural ventilation and rainwater harvesting systems to 
    enhance 
      environmental performance and sustainability.

    ## Conceptual Ideas by Cero9 Arquitectos
    Cristina and Efren’s vision for the Cherry Blossom Pavilion was to create a structure that 
    seamlessly 
    integrates with the natural beauty of the Jerte Valley while celebrating the region’s iconic 
    cherry blossoms. 
    Key conceptual ideas include:
    - **Organic Form**: Inspired by the delicate structure of cherry blossoms, the pavilion’s 
    design evokes 
      natural beauty and harmony.
    - **Aesthetic and Functional Integration**: The perforated metal skin not only enhances the 
    building’s 
      visual appeal but also contributes to its environmental performance.
    - **Sustainability**: Incorporating features like natural ventilation and rainwater 
    collection to align with 
      ecological principles.
    - **Contextual Sensitivity**: Designing a pavilion that complements and enhances the 
    surrounding landscape 
      of the Jerte Valley.

    """),
        html.Img(src="/static/images/cherry-blossom1.jpg", className="responsive-img"),
        dcc.Markdown("""
    ## Key Features
    - **Organic Design**: Fluid, petal-like form inspired by cherry blossoms.
    - **Perforated Metal Skin**: Creates dynamic light effects and provides aesthetic and 
    functional benefits.
    - **Lightweight Steel Framework**: Supports the pavilion’s complex geometry with minimal 
    material use.
    - **Sustainable Systems**: Features natural ventilation and rainwater harvesting for 
    environmental efficiency.
    - **Integration with Nature**: Reflects the natural beauty of the Jerte Valley and celebrates 
    local flora.

    """),
        html.Img(src="/static/images/cherry-blossom2.jpg", className="responsive-img"),
        dcc.Markdown("""
    The Cherry Blossom Pavilion by Cero9 Arquitectos stands as a remarkable example of how 
    contemporary 
    architecture can harmoniously blend with the natural landscape. The pavilion not only 
    celebrates the beauty 
    of the Jerte Valley but also showcases innovative design and engineering solutions that 
    reflect both aesthetic 
    and environmental considerations.

    """),
        html.Img(src="/static/images/cherry-blossom3.jpg", className="responsive-img")
    ])

}
cnte = {
    "src": """
    https://app.speckle.systems/projects/219ed1d96a/models/all#embed=%7B%22isEnabled%22%3Atrue
    %2C%22isTransparent%22%3Atrue%2C%22hideControls%22%3Atrue%2C%22hideSelectionInfo%22%3Atrue%7D
    """,
    "id": "alkjsf8d1d96a",
    "title": "CNTTE Building",
    # "badge": "badge-primary",
    "card_introduction": """
    The CNTTE Building, designed by the architectural firm Kohn Pedersen Fox, is a landmark 
    office tower in Beijing, China. Completed in 2018, this striking building stands out for its 
    innovative design and sustainable features. The tower's distinctive form is inspired by the 
    traditional Chinese lantern, with a faceted glass facade that
    reflects the surrounding landscape. The CNTTE Building incorporates advanced environmental
    technologies, including energy-efficient systems and green roofs, to reduce its environmental
    impact and enhance occupant comfort.
    """,

}

# TODO: Update this list with the new projects
params = [durango, mediatic, somisa, absolute, les_corts, zarzuela, pitch, castelar,
          shanghai, euskotren]
