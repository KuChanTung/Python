import logging
logging.basicConfig(level=logging.DEBUG)
from spyne import Application, rpc, ServiceBase, \
    Integer, Unicode
from spyne import Iterable
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

EmailString = Unicode.customize(
        max_length=128,
        pattern='[^@]+@[^@]+',
        type_name='EmailString',
    )

class EmailValidation(ServiceBase):
    @rpc(Unicode, EmailString, _returns=Unicode)
    def validate_email(ctx, username, email):
        return 'That is %s and %s' % (username, email)		
		
class HelloWorldService(ServiceBase):
    @rpc(Unicode, Integer, _returns=Iterable(Unicode))
    def say_hello(ctx, name, times):
        for i in range(times):
            yield 'Hello, %s' % name
			
application = Application([HelloWorldService, EmailValidation],
    tns='spyne.examples.hello',
    in_protocol=Soap11(),
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