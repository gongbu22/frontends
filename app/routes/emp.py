from fastapi import APIRouter, Request, Form
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from app.schema.emp import Employee

emp_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')

@emp_router.get('/', response_class=HTMLResponse)
async def emp(req: Request):
    return templates.TemplateResponse('emp/emp.html', {'request':req})

@emp_router.post('/', response_class=HTMLResponse)
async def empok(req: Request, empid= Form(...),
                fname= Form(...), lname= Form(...),
                email= Form(...), phone = Form(...),
                hdate = Form(...), jobid= Form(...),
                sal = Form(...), comm= Form(...),
                mgrid= Form(...), deptid= Form(...)):
    #
    # comm = comm if comm != 0.00 else None
    # mgrid = mgrid if mgrid != 0 else None
    # deptid = deptid if deptid != 0 else None
    emp = Employee(empid=empid, fname=fname, lname=lname,
              email=email, phone=phone, hdate=hdate, jobid=jobid,
              sal=sal, comm=comm, mgrid=mgrid, deptid=deptid)
    return templates.TemplateResponse('emp/result.html',
            {'request': req, 'emp': emp})
