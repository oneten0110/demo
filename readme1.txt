Traceback (most recent call last):
Traceback (most recent call last):
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen    
    response = self._make_request(
        conn,
    ...<10 lines>...
        **response_kw,
    )
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen    
    response = self._make_request(
        conn,
    ...<10 lines>...
        **response_kw,
    )
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 493, in _make_request
    conn.request(
    ~~~~~~~~~~~~^
        method,
        ^^^^^^^
    ...<6 lines>...
        enforce_content_length=enforce_content_length,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 493, in _make_request
    conn.request(
    ~~~~~~~~~~~~^
        method,
        ^^^^^^^
    ...<6 lines>...
        enforce_content_length=enforce_content_length,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "D:\grid\venv\Lib\site-packages\urllib3\connection.py", line 500, in request        
    self.endheaders()
    ~~~~~~~~~~~~~~~^^
  File "D:\grid\venv\Lib\site-packages\urllib3\connection.py", line 500, in request        
    self.endheaders()
    ~~~~~~~~~~~~~~~^^
  File "C:\Program Files\Python314\Lib\http\client.py", line 1353, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python314\Lib\http\client.py", line 1353, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python314\Lib\http\client.py", line 1113, in _send_output
    self.send(msg)
    ~~~~~~~~~^^^^^
  File "C:\Program Files\Python314\Lib\http\client.py", line 1113, in _send_output
    self.send(msg)
    ~~~~~~~~~^^^^^
  File "C:\Program Files\Python314\Lib\http\client.py", line 1057, in send
    self.connect()
    ~~~~~~~~~~~~^^
  File "C:\Program Files\Python314\Lib\http\client.py", line 1057, in send
    self.connect()
    ~~~~~~~~~~~~^^
  File "D:\grid\venv\Lib\site-packages\urllib3\connection.py", line 331, in connect        
    self.sock = self._new_conn()
                ~~~~~~~~~~~~~~^^
  File "D:\grid\venv\Lib\site-packages\urllib3\connection.py", line 331, in connect        
    self.sock = self._new_conn()
                ~~~~~~~~~~~~~~^^
  File "D:\grid\venv\Lib\site-packages\urllib3\connection.py", line 219, in _new_conn      
    raise NewConnectionError(
        self, f"Failed to establish a new connection: {e}"
    ) from e
  File "D:\grid\venv\Lib\site-packages\urllib3\connection.py", line 219, in _new_conn      
    raise NewConnectionError(
        self, f"Failed to establish a new connection: {e}"
    ) from e
urllib3.exceptions.NewConnectionError: HTTPConnection(host='localhost', port=4444): Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it
urllib3.exceptions.NewConnectionError: HTTPConnection(host='localhost', port=4444): Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

The above exception was the direct cause of the following exception:


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
Traceback (most recent call last):
  File "C:\Program Files\Python314\Lib\threading.py", line 1082, in _bootstrap_inner       
    self._context.run(self.run)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "C:\Program Files\Python314\Lib\threading.py", line 1082, in _bootstrap_inner       
    self._context.run(self.run)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "C:\Program Files\Python314\Lib\threading.py", line 1024, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python314\Lib\threading.py", line 1024, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\a.py", line 13, in run_test
    driver=webdriver.Remote(command_executor=GRID_URL,options=option)
  File "D:\grid\venv\a.py", line 13, in run_test
    driver=webdriver.Remote(command_executor=GRID_URL,options=option)
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\webdriver.py", line 271, in __init__
    self.start_session(capabilities)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\webdriver.py", line 271, in __init__
    self.start_session(capabilities)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\webdriver.py", line 366, in start_session
    response = self.execute(Command.NEW_SESSION, caps)["value"]
               ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\webdriver.py", line 366, in start_session
    response = self.execute(Command.NEW_SESSION, caps)["value"]
               ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\webdriver.py", line 443, in execute
    response = cast(RemoteConnection, self.command_executor).execute(driver_command, params)
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\webdriver.py", line 443, in execute
    response = cast(RemoteConnection, self.command_executor).execute(driver_command, params)
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\remote_connection.py", line 407, in execute
    return self._request(command_info[0], url, body=data)
           ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\remote_connection.py", line 431, in _request
    response = self._conn.request(method, url, body=body, headers=headers, timeout=self._client_config.timeout)
  File "D:\grid\venv\Lib\site-packages\urllib3\_request_methods.py", line 143, in request  
    return self.request_encode_body(
           ~~~~~~~~~~~~~~~~~~~~~~~~^
        method, url, fields=fields, headers=headers, **urlopen_kw
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\remote_connection.py", line 407, in execute
    return self._request(command_info[0], url, body=data)
           ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\Lib\site-packages\urllib3\_request_methods.py", line 278, in request_encode_body
    return self.urlopen(method, url, **extra_kw)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\remote_connection.py", line 431, in _request
    response = self._conn.request(method, url, body=body, headers=headers, timeout=self._client_config.timeout)
  File "D:\grid\venv\Lib\site-packages\urllib3\poolmanager.py", line 457, in urlopen       
    response = conn.urlopen(method, u.request_uri, **kw)
  File "D:\grid\venv\Lib\site-packages\urllib3\_request_methods.py", line 143, in request  
    return self.request_encode_body(
           ~~~~~~~~~~~~~~~~~~~~~~~~^
        method, url, fields=fields, headers=headers, **urlopen_kw
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 871, in urlopen    
    return self.urlopen(
           ~~~~~~~~~~~~^
        method,
        ^^^^^^^
    ...<13 lines>...
        **response_kw,
        ^^^^^^^^^^^^^^
    )
    ^
  File "D:\grid\venv\Lib\site-packages\urllib3\_request_methods.py", line 278, in request_encode_body
    return self.urlopen(method, url, **extra_kw)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 871, in urlopen    
    return self.urlopen(
           ~~~~~~~~~~~~^
        method,
        ^^^^^^^
    ...<13 lines>...
        **response_kw,
        ^^^^^^^^^^^^^^
    )
    ^
  File "D:\grid\venv\Lib\site-packages\urllib3\poolmanager.py", line 457, in urlopen       
    response = conn.urlopen(method, u.request_uri, **kw)
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 871, in urlopen    
    return self.urlopen(
           ~~~~~~~~~~~~^
        method,
        ^^^^^^^
    ...<13 lines>...
        **response_kw,
        ^^^^^^^^^^^^^^
    )
    ^
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 871, in urlopen    
    return self.urlopen(
           ~~~~~~~~~~~~^
        method,
        ^^^^^^^
    ...<13 lines>...
        **response_kw,
        ^^^^^^^^^^^^^^
    )
    ^
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 841, in urlopen    
    retries = retries.increment(
        method, url, error=new_e, _pool=self, _stacktrace=sys.exc_info()[2]
    )
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 871, in urlopen    
    return self.urlopen(
           ~~~~~~~~~~~~^
        method,
        ^^^^^^^
    ...<13 lines>...
        **response_kw,
        ^^^^^^^^^^^^^^
    )
    ^
  File "D:\grid\venv\Lib\site-packages\urllib3\util\retry.py", line 535, in increment      
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 871, in urlopen    
    return self.urlopen(
           ~~~~~~~~~~~~^
        method,
        ^^^^^^^
    ...<13 lines>...
        **response_kw,
        ^^^^^^^^^^^^^^
    )
    ^
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=4444): Max retries exceeded with url: /session (Caused by NewConnectionError("HTTPConnection(host='localhost', port=4444): Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it"))
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 841, in urlopen    
    retries = retries.increment(
        method, url, error=new_e, _pool=self, _stacktrace=sys.exc_info()[2]
    )
  File "D:\grid\venv\Lib\site-packages\urllib3\util\retry.py", line 535, in increment      
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=4444): Max retries exceeded with url: /session (Caused by NewConnectionError("HTTPConnection(host='localhost', port=4444): Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it"))

(venv) D:\grid\venv>python a.py
sucess grid
Exception in thread Thread-2 (run_test):
Exception in thread Thread-1 (run_test):
Traceback (most recent call last):
Traceback (most recent call last):
  File "D:\grid\venv\Lib\site-packages\urllib3\connection.py", line 204, in _new_conn      
    sock = connection.create_connection(
        (self._dns_host, self.port),
    ...<2 lines>...
        socket_options=self.socket_options,
    )
  File "D:\grid\venv\Lib\site-packages\urllib3\connection.py", line 204, in _new_conn      
    sock = connection.create_connection(
        (self._dns_host, self.port),
    ...<2 lines>...
        socket_options=self.socket_options,
    )
  File "D:\grid\venv\Lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    raise err
  File "D:\grid\venv\Lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    raise err
  File "D:\grid\venv\Lib\site-packages\urllib3\util\connection.py", line 73, in create_connection
    sock.connect(sa)
    ~~~~~~~~~~~~^^^^
  File "D:\grid\venv\Lib\site-packages\urllib3\util\connection.py", line 73, in create_connection
    sock.connect(sa)
    ~~~~~~~~~~~~^^^^
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

The above exception was the direct cause of the following exception:


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
Traceback (most recent call last):
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen    
    response = self._make_request(
        conn,
    ...<10 lines>...
        **response_kw,
    )
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen    
    response = self._make_request(
        conn,
    ...<10 lines>...
        **response_kw,
    )
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 493, in _make_request
    conn.request(
    ~~~~~~~~~~~~^
        method,
        ^^^^^^^
    ...<6 lines>...
        enforce_content_length=enforce_content_length,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 493, in _make_request
    conn.request(
    ~~~~~~~~~~~~^
        method,
        ^^^^^^^
    ...<6 lines>...
        enforce_content_length=enforce_content_length,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "D:\grid\venv\Lib\site-packages\urllib3\connection.py", line 500, in request        
    self.endheaders()
    ~~~~~~~~~~~~~~~^^
  File "D:\grid\venv\Lib\site-packages\urllib3\connection.py", line 500, in request        
    self.endheaders()
    ~~~~~~~~~~~~~~~^^
  File "C:\Program Files\Python314\Lib\http\client.py", line 1353, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python314\Lib\http\client.py", line 1353, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python314\Lib\http\client.py", line 1113, in _send_output
    self.send(msg)
    ~~~~~~~~~^^^^^
  File "C:\Program Files\Python314\Lib\http\client.py", line 1113, in _send_output
    self.send(msg)
    ~~~~~~~~~^^^^^
  File "C:\Program Files\Python314\Lib\http\client.py", line 1057, in send
    self.connect()
    ~~~~~~~~~~~~^^
  File "C:\Program Files\Python314\Lib\http\client.py", line 1057, in send
    self.connect()
    ~~~~~~~~~~~~^^
  File "D:\grid\venv\Lib\site-packages\urllib3\connection.py", line 331, in connect        
    self.sock = self._new_conn()
                ~~~~~~~~~~~~~~^^
  File "D:\grid\venv\Lib\site-packages\urllib3\connection.py", line 331, in connect        
    self.sock = self._new_conn()
                ~~~~~~~~~~~~~~^^
  File "D:\grid\venv\Lib\site-packages\urllib3\connection.py", line 219, in _new_conn      
    raise NewConnectionError(
        self, f"Failed to establish a new connection: {e}"
    ) from e
  File "D:\grid\venv\Lib\site-packages\urllib3\connection.py", line 219, in _new_conn      
    raise NewConnectionError(
        self, f"Failed to establish a new connection: {e}"
    ) from e
urllib3.exceptions.NewConnectionError: HTTPConnection(host='localhost', port=4444): Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it
urllib3.exceptions.NewConnectionError: HTTPConnection(host='localhost', port=4444): Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

The above exception was the direct cause of the following exception:


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
Traceback (most recent call last):
  File "C:\Program Files\Python314\Lib\threading.py", line 1082, in _bootstrap_inner
    self._context.run(self.run)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "C:\Program Files\Python314\Lib\threading.py", line 1082, in _bootstrap_inner       
    self._context.run(self.run)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "C:\Program Files\Python314\Lib\threading.py", line 1024, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python314\Lib\threading.py", line 1024, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\a.py", line 13, in run_test
    driver=webdriver.Remote(command_executor=GRID_URL,options=option)
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\webdriver.py", line 271, in __init__
    self.start_session(capabilities)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
  File "D:\grid\venv\a.py", line 13, in run_test
    driver=webdriver.Remote(command_executor=GRID_URL,options=option)
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\webdriver.py", line 366, in start_session
    response = self.execute(Command.NEW_SESSION, caps)["value"]
               ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\webdriver.py", line 443, in execute
    response = cast(RemoteConnection, self.command_executor).execute(driver_command, params)
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\webdriver.py", line 271, in __init__
    self.start_session(capabilities)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\remote_connection.py", line 407, in execute
    return self._request(command_info[0], url, body=data)
           ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\webdriver.py", line 366, in start_session
    response = self.execute(Command.NEW_SESSION, caps)["value"]
               ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\remote_connection.py", line 431, in _request
    response = self._conn.request(method, url, body=body, headers=headers, timeout=self._client_config.timeout)
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\webdriver.py", line 443, in execute
    response = cast(RemoteConnection, self.command_executor).execute(driver_command, params)
  File "D:\grid\venv\Lib\site-packages\urllib3\_request_methods.py", line 143, in request  
    return self.request_encode_body(
           ~~~~~~~~~~~~~~~~~~~~~~~~^
        method, url, fields=fields, headers=headers, **urlopen_kw
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\remote_connection.py", line 407, in execute
    return self._request(command_info[0], url, body=data)
           ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\Lib\site-packages\urllib3\_request_methods.py", line 278, in request_encode_body
    return self.urlopen(method, url, **extra_kw)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\remote_connection.py", line 431, in _request
    response = self._conn.request(method, url, body=body, headers=headers, timeout=self._client_config.timeout)
  File "D:\grid\venv\Lib\site-packages\urllib3\poolmanager.py", line 457, in urlopen       
    response = conn.urlopen(method, u.request_uri, **kw)
  File "D:\grid\venv\Lib\site-packages\urllib3\_request_methods.py", line 143, in request  
    return self.request_encode_body(
           ~~~~~~~~~~~~~~~~~~~~~~~~^
        method, url, fields=fields, headers=headers, **urlopen_kw
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 871, in urlopen    
    return self.urlopen(
           ~~~~~~~~~~~~^
        method,
        ^^^^^^^
    ...<13 lines>...
        **response_kw,
        ^^^^^^^^^^^^^^
    )
    ^
  File "D:\grid\venv\Lib\site-packages\urllib3\_request_methods.py", line 278, in request_encode_body
    return self.urlopen(method, url, **extra_kw)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 871, in urlopen    
    return self.urlopen(
           ~~~~~~~~~~~~^
        method,
        ^^^^^^^
    ...<13 lines>...
        **response_kw,
        ^^^^^^^^^^^^^^
    )
    ^
  File "D:\grid\venv\Lib\site-packages\urllib3\poolmanager.py", line 457, in urlopen       
    response = conn.urlopen(method, u.request_uri, **kw)
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 871, in urlopen    
    return self.urlopen(
           ~~~~~~~~~~~~^
        method,
        ^^^^^^^
    ...<13 lines>...
        **response_kw,
        ^^^^^^^^^^^^^^
    )
    ^
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 871, in urlopen    
    return self.urlopen(
           ~~~~~~~~~~~~^
        method,
        ^^^^^^^
    ...<13 lines>...
        **response_kw,
        ^^^^^^^^^^^^^^
    )
    ^
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 841, in urlopen    
    retries = retries.increment(
        method, url, error=new_e, _pool=self, _stacktrace=sys.exc_info()[2]
    )
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 871, in urlopen    
    return self.urlopen(
           ~~~~~~~~~~~~^
        method,
        ^^^^^^^
    ...<13 lines>...
        **response_kw,
        ^^^^^^^^^^^^^^
    )
    ^
  File "D:\grid\venv\Lib\site-packages\urllib3\util\retry.py", line 535, in increment      
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 871, in urlopen    
    return self.urlopen(
           ~~~~~~~~~~~~^
        method,
        ^^^^^^^
    ...<13 lines>...
        **response_kw,
        ^^^^^^^^^^^^^^
    )
    ^
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=4444): Max retries exceeded with url: /session (Caused by NewConnectionError("HTTPConnection(host='localhost', port=4444): Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it"))
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 841, in urlopen    
    retries = retries.increment(
        method, url, error=new_e, _pool=self, _stacktrace=sys.exc_info()[2]
    )
  File "D:\grid\venv\Lib\site-packages\urllib3\util\retry.py", line 535, in increment      
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=4444): Max retries exceeded with url: /session (Caused by NewConnectionError("HTTPConnection(host='localhost', port=4444): Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it"))

(venv) D:\grid\venv>python a.py
sucess grid
Exception in thread Thread-2 (run_test):
Exception in thread Thread-1 (run_test):
Traceback (most recent call last):
Traceback (most recent call last):
  File "D:\grid\venv\Lib\site-packages\urllib3\connection.py", line 204, in _new_conn      
    sock = connection.create_connection(
        (self._dns_host, self.port),
    ...<2 lines>...
        socket_options=self.socket_options,
    )
  File "D:\grid\venv\Lib\site-packages\urllib3\connection.py", line 204, in _new_conn      
    sock = connection.create_connection(
        (self._dns_host, self.port),
    ...<2 lines>...
        socket_options=self.socket_options,
    )
  File "D:\grid\venv\Lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    raise err
  File "D:\grid\venv\Lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    raise err
  File "D:\grid\venv\Lib\site-packages\urllib3\util\connection.py", line 73, in create_connection
    sock.connect(sa)
    ~~~~~~~~~~~~^^^^
  File "D:\grid\venv\Lib\site-packages\urllib3\util\connection.py", line 73, in create_connection
    sock.connect(sa)
    ~~~~~~~~~~~~^^^^
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

The above exception was the direct cause of the following exception:


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
Traceback (most recent call last):
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen    
    response = self._make_request(
        conn,
    ...<10 lines>...
        **response_kw,
    )
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen    
    response = self._make_request(
        conn,
    ...<10 lines>...
        **response_kw,
    )
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 493, in _make_request
    conn.request(
    ~~~~~~~~~~~~^
        method,
        ^^^^^^^
    ...<6 lines>...
        enforce_content_length=enforce_content_length,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 493, in _make_request
    conn.request(
    ~~~~~~~~~~~~^
        method,
        ^^^^^^^
    ...<6 lines>...
        enforce_content_length=enforce_content_length,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "D:\grid\venv\Lib\site-packages\urllib3\connection.py", line 500, in request        
    self.endheaders()
    ~~~~~~~~~~~~~~~^^
  File "D:\grid\venv\Lib\site-packages\urllib3\connection.py", line 500, in request        
    self.endheaders()
    ~~~~~~~~~~~~~~~^^
  File "C:\Program Files\Python314\Lib\http\client.py", line 1353, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python314\Lib\http\client.py", line 1353, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python314\Lib\http\client.py", line 1113, in _send_output
    self.send(msg)
    ~~~~~~~~~^^^^^
  File "C:\Program Files\Python314\Lib\http\client.py", line 1113, in _send_output
    self.send(msg)
    ~~~~~~~~~^^^^^
  File "C:\Program Files\Python314\Lib\http\client.py", line 1057, in send
    self.connect()
    ~~~~~~~~~~~~^^
  File "C:\Program Files\Python314\Lib\http\client.py", line 1057, in send
    self.connect()
    ~~~~~~~~~~~~^^
  File "D:\grid\venv\Lib\site-packages\urllib3\connection.py", line 331, in connect        
    self.sock = self._new_conn()
                ~~~~~~~~~~~~~~^^
  File "D:\grid\venv\Lib\site-packages\urllib3\connection.py", line 331, in connect        
    self.sock = self._new_conn()
                ~~~~~~~~~~~~~~^^
  File "D:\grid\venv\Lib\site-packages\urllib3\connection.py", line 219, in _new_conn      
    raise NewConnectionError(
        self, f"Failed to establish a new connection: {e}"
    ) from e
  File "D:\grid\venv\Lib\site-packages\urllib3\connection.py", line 219, in _new_conn      
    raise NewConnectionError(
        self, f"Failed to establish a new connection: {e}"
    ) from e
urllib3.exceptions.NewConnectionError: HTTPConnection(host='localhost', port=4444): Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it
urllib3.exceptions.NewConnectionError: HTTPConnection(host='localhost', port=4444): Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it

The above exception was the direct cause of the following exception:


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
Traceback (most recent call last):
  File "C:\Program Files\Python314\Lib\threading.py", line 1082, in _bootstrap_inner       
    self._context.run(self.run)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "C:\Program Files\Python314\Lib\threading.py", line 1082, in _bootstrap_inner       
    self._context.run(self.run)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "C:\Program Files\Python314\Lib\threading.py", line 1024, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python314\Lib\threading.py", line 1024, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\a.py", line 13, in run_test
    driver=webdriver.Remote(command_executor=GRID_URL,options=option)
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\webdriver.py", line 271, in __init__
    self.start_session(capabilities)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
  File "D:\grid\venv\a.py", line 13, in run_test
    driver=webdriver.Remote(command_executor=GRID_URL,options=option)
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\webdriver.py", line 366, in start_session
    response = self.execute(Command.NEW_SESSION, caps)["value"]
               ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\webdriver.py", line 271, in __init__
    self.start_session(capabilities)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\webdriver.py", line 443, in execute
    response = cast(RemoteConnection, self.command_executor).execute(driver_command, params)
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\webdriver.py", line 366, in start_session
    response = self.execute(Command.NEW_SESSION, caps)["value"]
               ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\remote_connection.py", line 407, in execute
    return self._request(command_info[0], url, body=data)
           ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\webdriver.py", line 443, in execute
    response = cast(RemoteConnection, self.command_executor).execute(driver_command, params)
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\remote_connection.py", line 431, in _request
    response = self._conn.request(method, url, body=body, headers=headers, timeout=self._client_config.timeout)
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\remote_connection.py", line 407, in execute
    return self._request(command_info[0], url, body=data)
           ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\Lib\site-packages\urllib3\_request_methods.py", line 143, in request  
    return self.request_encode_body(
           ~~~~~~~~~~~~~~~~~~~~~~~~^
        method, url, fields=fields, headers=headers, **urlopen_kw
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\remote_connection.py", line 431, in _request
    response = self._conn.request(method, url, body=body, headers=headers, timeout=self._client_config.timeout)
  File "D:\grid\venv\Lib\site-packages\urllib3\_request_methods.py", line 278, in request_encode_body
    return self.urlopen(method, url, **extra_kw)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\Lib\site-packages\urllib3\poolmanager.py", line 457, in urlopen       
    response = conn.urlopen(method, u.request_uri, **kw)
  File "D:\grid\venv\Lib\site-packages\urllib3\_request_methods.py", line 143, in request  
    return self.request_encode_body(
           ~~~~~~~~~~~~~~~~~~~~~~~~^
        method, url, fields=fields, headers=headers, **urlopen_kw
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 871, in urlopen    
    return self.urlopen(
           ~~~~~~~~~~~~^
        method,
        ^^^^^^^
    ...<13 lines>...
        **response_kw,
        ^^^^^^^^^^^^^^
    )
    ^
  File "D:\grid\venv\Lib\site-packages\urllib3\_request_methods.py", line 278, in request_encode_body
    return self.urlopen(method, url, **extra_kw)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 871, in urlopen    
    return self.urlopen(
           ~~~~~~~~~~~~^
        method,
        ^^^^^^^
    ...<13 lines>...
        **response_kw,
        ^^^^^^^^^^^^^^
    )
    ^
  File "D:\grid\venv\Lib\site-packages\urllib3\poolmanager.py", line 457, in urlopen       
    response = conn.urlopen(method, u.request_uri, **kw)
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 871, in urlopen    
    return self.urlopen(
           ~~~~~~~~~~~~^
        method,
        ^^^^^^^
    ...<13 lines>...
        **response_kw,
        ^^^^^^^^^^^^^^
    )
    ^
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 871, in urlopen    
    return self.urlopen(
           ~~~~~~~~~~~~^
        method,
        ^^^^^^^
    ...<13 lines>...
        **response_kw,
        ^^^^^^^^^^^^^^
    )
    ^
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 841, in urlopen    
    retries = retries.increment(
        method, url, error=new_e, _pool=self, _stacktrace=sys.exc_info()[2]
    )
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 871, in urlopen    
    return self.urlopen(
           ~~~~~~~~~~~~^
        method,
        ^^^^^^^
    ...<13 lines>...
        **response_kw,
        ^^^^^^^^^^^^^^
    )
    ^
  File "D:\grid\venv\Lib\site-packages\urllib3\util\retry.py", line 535, in increment      
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 871, in urlopen    
    return self.urlopen(
           ~~~~~~~~~~~~^
        method,
        ^^^^^^^
    ...<13 lines>...
        **response_kw,
        ^^^^^^^^^^^^^^
    )
    ^
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=4444): Max retries exceeded with url: /session (Caused by NewConnectionError("HTTPConnection(host='localhost', port=4444): Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it"))
  File "D:\grid\venv\Lib\site-packages\urllib3\connectionpool.py", line 841, in urlopen    
    retries = retries.increment(
        method, url, error=new_e, _pool=self, _stacktrace=sys.exc_info()[2]
    )
  File "D:\grid\venv\Lib\site-packages\urllib3\util\retry.py", line 535, in increment      
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=4444): Max retries exceeded with url: /session (Caused by NewConnectionError("HTTPConnection(host='localhost', port=4444): Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it"))

(venv) D:\grid\venv>python a.py
sucess grid
Exception in thread Thread-2 (run_test):
Traceback (most recent call last):
  File "C:\Program Files\Python314\Lib\threading.py", line 1082, in _bootstrap_inner       
    self._context.run(self.run)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "C:\Program Files\Python314\Lib\threading.py", line 1024, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\a.py", line 16, in run_test
    driver.get("file//" +os.pat.abspath("c.html"))
                         ^^^^^^
AttributeError: module 'os' has no attribute 'pat'. Did you mean: 'path'?
Exception in thread Thread-1 (run_test):
Traceback (most recent call last):
  File "C:\Program Files\Python314\Lib\threading.py", line 1082, in _bootstrap_inner       
    self._context.run(self.run)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "C:\Program Files\Python314\Lib\threading.py", line 1024, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\a.py", line 16, in run_test
    driver.get("file//" +os.pat.abspath("c.html"))
                         ^^^^^^
AttributeError: module 'os' has no attribute 'pat'. Did you mean: 'path'?

(venv) D:\grid\venv>python a.py
sucess grid
Exception in thread Thread-2 (run_test):
Traceback (most recent call last):
  File "C:\Program Files\Python314\Lib\threading.py", line 1082, in _bootstrap_inner       
    self._context.run(self.run)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "C:\Program Files\Python314\Lib\threading.py", line 1024, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\a.py", line 16, in run_test
    driver.get("file//" +os.pat.abspath("c.html"))
                         ^^^^^^
AttributeError: module 'os' has no attribute 'pat'. Did you mean: 'path'?
Exception in thread Thread-1 (run_test):
Traceback (most recent call last):
  File "C:\Program Files\Python314\Lib\threading.py", line 1082, in _bootstrap_inner       
    self._context.run(self.run)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "C:\Program Files\Python314\Lib\threading.py", line 1024, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\a.py", line 16, in run_test
    driver.get("file//" +os.pat.abspath("c.html"))
                         ^^^^^^
AttributeError: module 'os' has no attribute 'pat'. Did you mean: 'path'?

(venv) D:\grid\venv>python a.py
sucees grid
Exception in thread Thread-2 (run_test):
Traceback (most recent call last):
  File "C:\Program Files\Python314\Lib\threading.py", line 1082, in _bootstrap_inner       
    self._context.run(self.run)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "C:\Program Files\Python314\Lib\threading.py", line 1024, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\a.py", line 26, in run_test
    driver.find_element(By.ID,"downloadBtn").click()
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\webelement.py", line 114, in click
    self._execute(Command.CLICK_ELEMENT)
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\webelement.py", line 508, in _execute
    return self._parent.execute(command, params)
           ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\webdriver.py", line 446, in execute
    self.error_handler.check_response(response)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 232, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable
  (Session info: MicrosoftEdge=145.0.3800.97); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#elementnotinteractableexception
Stacktrace:
Symbols not available. Dumping unresolved backtrace:
        0x7ff76ea87c25
        0x7ff76ea87c84
        0x7ff76e7dacee
        0x7ff76e824a28
        0x7ff76e81a8bd
        0x7ff76e8442ba
        0x7ff76e81a307
        0x7ff76e81a20d
        0x7ff76e81a307
        0x7ff76e85f1e7
        0x7ff76e819a1c
        0x7ff76e818c76
        0x7ff76e819843
        0x7ff76e8e0564
        0x7ff76e8dca03
        0x7ff76e8ed0c3
        0x7ff76eaa2308
        0x7ff76eaaabe6
        0x7ff76ea8f264
        0x7ff76ea8f3a9
        0x7ff76ea7d1e2
        0x7ff936d2e8d7
        0x7ff93824c40c

Exception in thread Thread-1 (run_test):
Traceback (most recent call last):
  File "C:\Program Files\Python314\Lib\threading.py", line 1082, in _bootstrap_inner       
    self._context.run(self.run)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "C:\Program Files\Python314\Lib\threading.py", line 1024, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\a.py", line 26, in run_test
    driver.find_element(By.ID,"downloadBtn").click()
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\webelement.py", line 114, in click
    self._execute(Command.CLICK_ELEMENT)
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\webelement.py", line 508, in _execute
    return self._parent.execute(command, params)
           ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\webdriver.py", line 446, in execute
    self.error_handler.check_response(response)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "D:\grid\venv\Lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 232, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable
  (Session info: chrome=145.0.7632.160); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#elementnotinteractableexception
Stacktrace:
Symbols not available. Dumping unresolved backtrace:
        0x7ff623d7aa55
        0x7ff623ad8630
        0x7ff62386d546
        0x7ff6238c9bd4
        0x7ff6238bb426
        0x7ff6238f19da
        0x7ff6238baca6
        0x7ff62391591c
        0x7ff6238b9098
        0x7ff6238b9f83
        0x7ff623da7810
        0x7ff623da1afd
        0x7ff623dc2c1a
        0x7ff623af3345
        0x7ff623afb81c
        0x7ff623ae1924
        0x7ff623ae1ad6
        0x7ff623ac7e47
        0x7ff936d2e8d7
        0x7ff93824c40c


(venv) D:\grid\venv>python a.py
sucees grid

(venv) D:\grid\venv>python a.py
sucees grids

(venv) D:\grid\venv>git push
Everything up-to-date

(venv) D:\grid\venv>git add .

(venv) D:\grid\venv>git add .

(venv) D:\grid\venv>git commit -m "this is for docker"
[main 479b93b] this is for docker
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 dockerfile
 create mode 100644 script.py

(venv) D:\grid\venv>git push                          
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 12 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (2/2), 266 bytes | 266.00 KiB/s, done.
Total 2 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/oneten0110/demo
   8096135..479b93b  main -> main

(venv) D:\grid\venv>git commit -m "this is for docker1"
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   dockerfile
        modified:   script.py

no changes added to commit (use "git add" and/or "git commit -a")

(venv) D:\grid\venv>git push
Everything up-to-date

(venv) D:\grid\venv>git add .

(venv) D:\grid\venv>git commit -m "this is for docker1"
[main 5829b42] this is for docker1
 2 files changed, 26 insertions(+)

(venv) D:\grid\venv>git push
Enumerating objects: 7, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 12 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 619 bytes | 619.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/oneten0110/demo
   479b93b..5829b42  main -> main

(venv) D:\grid\venv>docker build -t selenium.
'docker' is not recognized as an internal or external command,
operable program or batch file.

(venv) D:\grid\venv> 