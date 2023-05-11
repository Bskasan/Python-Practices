
#* Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

#* User < - > Django < - > Url < - > View < - > Model < - > Database
#* A user request for a resource to the Django, Django works as a controller and check to the available resource in URL (urls.py file). if URL maps, a view (function) is called that interact with model and template, it renders a template. Django responds back to the user and sends a template as a response.

#? MVC (Model-View-Controller) is a pattern in software design commonly used to implement user interfaces, data, and controlling logic. It emphasizes a separation between the software's business logic and display. This "separation of concerns" provides for a better division of labor and improved maintenance.

#! FOR LOCAL SETUP (PYTHON DEFAULT SETUP -> GLOBAl)
#! python -m venv env
#! source env/Scripts/activate