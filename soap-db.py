import logging
logging.basicConfig(level=logging.DEBUG)
from spyne import Application, rpc, ServiceBase, \
    Integer, Unicode, ComplexModel, Array
from spyne import Iterable
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import sqlite3 as sql

class Task(ComplexModel):
    Uri = Unicode
    Title = Unicode
    Description = Unicode
    Done = Integer

class TaskList(ComplexModel):
    alltasks = 	Array(Task)
	
class getTask(ServiceBase):
    @rpc(Unicode, _returns=Task)
    def getInformationOfTask(ctx, Uri):
        conn = sql.connect('database.db')
        cur = conn.cursor()
        cur.execute("select * from Tasks where Uri=(?)", (Uri,))
        row = cur.fetchone()
		
        task = Task()
        task.Uri = row[0]
        task.Title = row[1]
        task.Description = row[2]
        task.Done = row[3]
        conn.close()
        return task		

class getAllTasks(ServiceBase):
    @rpc( _returns=TaskList)
    def getAllTasksInDB(ctx):
        conn = sql.connect('database.db')
        cur = conn.cursor()
        cur.execute("select * from Tasks")
        rows = cur.fetchall()
		
        tasklist = TaskList()
        tasklist.alltasks = []
        for row in rows:
            task = Task()
            task.Uri = row[0]
            task.Title = row[1]
            task.Description = row[2]
            task.Done = row[3]
            tasklist.alltasks.append(task)
		
        conn.close()
        return tasklist	
			
application = Application([getTask, getAllTasks],
    tns='spyne.examples.hello',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)
if __name__ == '__main__':
    # You can use any Wsgi server. Here, we chose
    # Python's built-in wsgi server but you're not
    # supposed to use it in production.
    from wsgiref.simple_server import make_server
    wsgi_app = WsgiApplication(application)
    server = make_server('0.0.0.0', 8000, wsgi_app)
    server.serve_forever()