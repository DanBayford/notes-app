note_1_title = "Next JS"
note_1_content = """React is often described as a framework, but it is more accurately a JavaScript UI library. It focuses solely on rendering components and managing UI state.

In contrast, full frameworks like Angular provide additional built-in functionality such as routing, state management, and data handling. With React, those features are usually provided by third-party libraries such as React Router (routing), Redux or Zustand (state), and TanStack Query (server data fetching and caching).

Next.js is a true framework built on React. It adds common application-level features out of the box, including:

	•	File-based routing
	•	Automatic code splitting
	•	Server-side rendering (SSR)
	•	Static site generation (SSG) and incremental static regeneration (ISR)
	•	Server actions and API routes

Together, these make Next.js what can be considered a complete framework, while React remains a flexible UI building block.
"""
note_2_title = "React Hooks"
note_2_content = """Hooks are functions that let React function components use state, refs, context, and lifecycle features during the render process.

React provides a set of built-in hooks. Common ones include:
	•	useState -> store data across renders and trigger rerenders.
	•	useEffect -> synchronize with systems outside React’s control (APIs, subscriptions, localStorage).
	•	useRef -> hold a mutable value or reference to a DOM node across renders without triggering rerenders.
	•	useContext -> consume values from a context object (created with React.createContext) provided higher up the tree.

Other hooks like useCallback and useMemo help avoid unnecessary rerenders by stabilizing function or object references. In React 19, the compiler often performs these optimizations automatically, so manual usage is less common, though still available.

You can also create custom hooks to encapsulate reusable logic. Each call to a custom hook is isolated — hooks don’t share state between component instances (unlike context, which provides shared state).

React enforces the “Rules of Hooks”: they must be called at the top level of components (or other hooks), in the same order on every render, and not conditionally. This ensures React can correctly map each hook call to its internal state.
"""
note_3_title = "Docker Compose"
note_3_content = """Docker Compose is a tool that simplifies the configuration and running of multiple Docker containers. 

Instead of individually running commands for each container and manually setting up networks and volumes, a single Compose YAML file can be used.

Inside the Compose file, you can configure things such as:
  • The services (individual) containers to run
  • The startup sequence of the containers (although note this is the contaienr startup - not necessarily the service readiness)
  • Where to find environment variables
  • What ports to expose
  • Container startup commands
  • Container volume binds
  • Container networks

This makes complex applications more predictable and repeatable.
"""
note_4_title = "Python Collections"
note_4_content ="""Python collections are built-in data types that let you group, organize, and manage multiple values. The most commonly used are lists, tuples, dictionaries, and sets:

	•	list → ordered, mutable sequence.
	•	tuple → ordered, immutable sequence.
	•	dict (dictionary) → key–value pairs, insertion-ordered since Python 3.7.
	•	set → unordered collection of unique elements.

Lists and tuples are indexed sequences and can store any type of object, including other collections.

Dictionary keys must be unique and hashable (immutable types like strings, numbers, and tuples are common), which allows Python to implement dictionaries as hash tables — giving very fast lookups.

Sets also use hashing and enforce uniqueness, making them useful for removing duplicates or testing membership efficiently.

All of these collections are iterable, so they can be used in for loops, comprehensions, map(), and other constructs that operate on sequences.
"""
note_5_title = "SSH"
note_5_content ="""Secure Shell, or SSH, is a cryptographic protocol for securely logging in to and managing remote systems over an untrusted network.

Like HTTPS, it runs on top of TCP/IP and relies on public–private key cryptography, but the way it establishes trust and secures the session is different. SSH does not use certificates from third-party authorities; instead, it relies on host keys and direct key exchange between client and server.

When a client attempts to log in with a key, the server issues a random challenge. The client uses its private key to generate a digital signature over this challenge. Because of the mathematics of the key pair, only the holder of the private key can produce a valid signature.

The client returns this signature, and the server verifies it using the corresponding public key from the user’s authorized_keys. The server does not need the private key to do this.

If verification succeeds, the server is confident that the client possesses the private key, and a symmetric session key is then established to encrypt all subsequent traffic.
"""
note_6_title = "HTTPS"
note_6_content = """With normal HTTP, requests and responses are sent in plaintext: both headers and body can be read by anyone intercepting network traffic (e.g., with a Wi-Fi sniffer). While the body may optionally be compressed (e.g., gzip), the data is not encrypted and can be trivially reconstructed.

HTTPS is a secure version of HTTP that encrypts both headers and body using symmetric cryptography. Even if intercepted, the data remains confidential as long as the session key is secret. Some metadata — such as IP addresses, ports, etc — remain visible for routing purposes.

When an HTTPS session is initiated, the client and server establish a secure TLS connection over TCP. During the TLS handshake, they use asymmetric cryptography: the server proves its identity with a certificate signed by a trusted authority, while an agreed key exchange procedure is used to derive a shared symmetric session key. Once the handshake is complete, all HTTP traffic is encrypted with that session key.
"""
note_7_title = "Closures"
note_7_content = """A closure is a feature of JavaScript where a function retains access to variables from its lexical scope, even after the outer function has finished executing. It is often seen when a function returns another function.

For example, suppose function a defines a variable x and returns function b, which increments and returns x. If we call a and store the result (the reference to b), function a has already returned, so you might expect x to no longer exist.

However, when we call b, x is incremented and persists across calls. Each subsequent call to b further increments x.

This works because function b “closes over” the environment in which it was created. Although a’s execution context has ended, its lexical environment — including x — is preserved by the closure and remains accessible to b.
"""
note_8_title = "Encryption"
note_8_content = """Encryption is the process of converting human-readable plaintext into unreadable ciphertext using a cryptographic key, while decryption is the reverse. Only parties with the correct key(s) can recover the original message. The algorithms themselves are public; security comes from the secrecy of the key.

There are two main types of encryption. Symmetric encryption uses the same key for both encryption and decryption. Asymmetric encryption (public-key cryptography) uses a key pair: a public key, usually for encryption, and a private key for decryption. This means anyone can encrypt data for the private key holder, but only they can decrypt it. The private key can also be used to sign data, with the public key verifying authenticity.

Protocols such as HTTPS and SSH combine the two: asymmetric encryption secures the exchange of a shared session key, after which symmetric encryption is used for efficient, secure communication.
"""
note_9_title = "CSRF"
note_9_content = """Cross-Site Request Forgery (CSRF) is an attack where a victim’s browser is tricked into sending authenticated requests that the user did not intend.

When you are logged into a service, such as online banking, the site sets cookies on your browser to maintain session state. Any subsequent request to that site automatically includes those cookies.

In a CSRF attack, an attacker embeds a malicious request (for example, a hidden form or crafted link) that your browser submits while you are logged in. Because the request includes your valid session cookies, the site treats it as legitimate and may carry out actions such as transferring money or changing account settings without your knowledge.

Mitigations include:
	•	CSRF tokens — servers embed random tokens in legitimate forms or headers, which must match the session; attackers cannot predict them.
	•	SameSite cookies — instruct browsers not to send cookies on cross-site requests.
	•	Reauthentication / user interaction — requiring re-login, confirmation prompts, or CAPTCHAs for sensitive operations.
"""
note_10_title = "Cross Site Scripting"
note_10_content = """Cross-Site Scripting (XSS) is an attack where malicious JavaScript is injected into a trusted web page and executed in the victim’s browser. This can be used to steal data from localStorage or sessionStorage, read cookies that are not marked HttpOnly, or perform actions on behalf of the user by issuing requests with their session.

XSS generally comes in three forms:
	•	Stored XSS -> the payload is saved on the server (database, cache, CMS, etc.) and delivered to other users (e.g. unsanitized forum comments).
	•	Reflected XSS -> the payload is included in a request (query param, form field) and reflected directly into the HTML response (e.g. a search page echoing user input).
	•	DOM-based XSS -> the payload is executed entirely client-side when insecure frontend code inserts attacker-controlled values into the DOM (e.g. using innerHTML).

Mitigations include:
	•	Escaping and sanitising output so user input can never be interpreted as code.
	•	Validating and filtering input to reduce obvious dangerous patterns.
	•	Using a Content Security Policy (CSP) to restrict which scripts can run, reducing the impact of injected code.
"""
note_11_title = "Context API"
note_11_content = """The Context API is a set of functions provided by React that allows an application to pass values to nested components without so called 'prop-drilling.'

It is essentially an implementation of the dependency injection pattern, where a provider gives access to a value when requested by a subscriber.

It is referred to as an API as it provides several mechanisms to set up the dependency container and consume the context:

  • A context object to initialise the context value(s) and set defaults
  • A context provider that provides the context value(s) to any child components that might request it
  • A context hook (useContext) to access the context value(s) from within a component

A commmon pattern is to abstract the context behind a dedicated hook so the context object does not have to be imported everywhere it is requested via useContext.

Note that it is generally not recommended to pass rapidly changing values via context as it can cause excessive rerendering.
"""
note_12_title = "Django Models"
note_12_content = """A Django model is a Python representation of a database table that Django uses to map between Python objects and database rows. Generally speaking, each model can be thought of as a table, and then the individual attributes as the table columns. 

For Django to identify a class as a model and therefore add it to the database and track any subsequent changes via its migration system, it needs to inherit from the models.Model parent class. This also gives the model certain core beviours that can be overriden ia usual OOP principles.

Attributes are defined with a particular field type so that the migration system can create and edit the appropriate field for the underlying database (VARCHAR etc). Each field may then have extra constraints or context such as minimum length, a FK reference or nullability.

Django models also have a Meta subclass where other behaviour can be defined, such as database constraints or default ordering when read from the table.

Once created, models can be interacted with using the Django ORM. This gives a rich API of common functionality (eg get, delete, filter), allowing you to interact with your databse in a more Pythonic way. It also handles things like query parameterization automatically to prevent SQL injection.
"""
note_13_title = "Cookies"
note_13_content = """A cookie is a small piece of data that a server sets in the user’s browser via the Set-Cookie header. On subsequent requests to the same domain, the browser automatically includes the cookie, making it possible to maintain state across otherwise stateless HTTP connections.

Cookies are commonly used for session management (e.g. authentication), saving user preferences, and tracking users for analytics.

Each cookie has attributes that control its behavior:
	•	Domain/Path -> define which requests include the cookie.
	•	Expires/Max-Age -> determine how long it is valid.
	•	Secure -> only sent over HTTPS.
	•	HttpOnly -> prevents client-side JavaScript access, mitigating XSS.
	•	SameSite -> restricts cross-site sending to mitigate CSRF.

SameSite options:
	•	Strict -> cookies only sent for requests from the same site.
	•	Lax -> also sent on top-level navigation from other sites (e.g. following a link), but not with cross-site POSTs or iframes.
	•	None -> cookies sent in all contexts, but must also use Secure.

Most browsers limit cookies to ~4KB each and ~50 per domain.
"""
note_14_title = "Wagtail CMS"
note_14_content = """Wagtail is a CMS built on top of the Django web framework, used by organisations such as NASA, Mozilla, and Oxfam.

It extends Django’s core functionality (ORM, request handling, MVT pattern) with it's own Page model and a rich admin interface with editorial workflows.

At its heart is the abstract Page model, which developers subclass to define different content types. Wagtail automatically provides features like revision history, moderation, and publishing controls for these pages. 

Pages are organised in a hierarchical tree using the Treebeard library, allowing parent/child relationships and clean URL structures.

Wagtail also includes the StreamField field type, which stores content in a sequence of blocks (text, images, embeds, or custom content types) that editors can reorder and combine to build flexible page layouts.

The Wagtail admin is designed for non-technical users (ie content editors), with a modern UI and support for custom workflows, scheduling, and page previewing. 

Wagtail can manage an entire Django site or just a section of its URL space. It can also operate headless if you want it as simply a datastore.
"""
note_15_title = "Docker Images and Containers"
note_15_content = """Docker is a platform for developing, sharing, and running applications inside lightweight environments called containers. Instead of running directly on the host system with all its dependencies, an application runs inside a container that isolates it from the rest of the machine while still sharing the host’s operating system kernel.

This approach helps solve many common issues in software development where code works on one machine but fails on another. By packaging the application together with its runtime, libraries, and configuration, Docker effectively moves the environment along with the application, ensuring consistent behavior across development, testing, and production.

The two core concepts in Docker are images and containers.

An image is a read-only template that defines the container’s environment. It typically starts from a base image (e.g. Linux, Node, Python) and adds layers with dependencies, configuration, and application code. Images are defined by a Dockerfile, which can be shared and rebuilt consistently across systems.

A container is a running instance of an image. Once an image is available, containers can be started, stopped, paused, or removed. They are much lighter than traditional virtual machines because they reuse the host OS kernel, rather than starting up separate guest operating systems with their own kernels.
"""
note_16_title = "Tailwind CSS"
note_16_content = """Tailwind CSS is a utility-first CSS framework that provides a rich set of low-level classes for styling elements directly in your markup.

Traditionally, there were two main approaches to styling:
	•	Custom CSS stylesheets, often structured with patterns like BEM to attempt to keep codebases organized.
	•	UI frameworks such as Bootstrap, which provide pre-styled components (headers, cards, buttons) applied via a single class.

Custom CSS can be difficult to maintain consistently across a large project, while UI frameworks often lead to “samey” looking sites that share the same visual identity.

Tailwind takes a different approach: it offers a comprehensive set of small, single-purpose classes (p-4, text-center, bg-blue-500, etc.) that can be composed to build entirely custom designs without writing separate CSS files. This balances flexibility with consistency.

During the build process, Tailwind generates only the classes you actually use, automatically applies vendor prefixes, and integrates with tools to minify the output. The result is a smaller, optimized stylesheet that loads quickly in the browser.
"""
note_17_title = "Relational Databases"
note_17_content = """Relational databases store data in tables, and these tables often have relationships with each other. This reduces duplication and enforces integrity. Relationships are usually implemented through foreign keys — references to rows in another table.

	•	One-to-One (1:1) -> each row in one table can be associated with at most one row in another table. Often used to extend a table without adding more columns (e.g. User and UserProfile).
	•	One-to-Many (1:N) -> a row in one table can be related to multiple rows in another, but each row in the second table relates back to only one in the first (e.g. Customer ↔ Orders).
	•	Many-to-Many (M:N) -> rows in one table can relate to multiple rows in another, and vice versa. This is usually implemented via a junction table that holds foreign keys to both tables (e.g. Students ↔ Courses).
	•	Self-referencing -> a table can relate to itself, such as an Employee table with a manager_id referencing another Employee.
"""
note_18_title = "Hoisting"
note_18_content = """Hoisting is JavaScript’s behavior of conceptually “moving” some variable and function declarations to the top of their scope before code execution. This is only conceptual — the code isn’t physically reordered, but it appears that way in practice.

	•	Function declarations are fully hoisted, including their body. This means you can call a function before it 'appears' in the source code.
	•	var declarations are hoisted and automatically initialized with undefined. Accessing them before assignment returns undefined.
	•	let and const declarations are also hoisted, but not initialized. They remain in the Temporal Dead Zone (TDZ) until execution reaches their declaration, and accessing them early throws a ReferenceError.
  
A common source of confusion is that function expressions or arrow functions assigned to variables are hoisted according to the variable type (var, let, or const), unlike function declarations.
"""
note_19_title = "React Lazy Loading and Suspense"
note_19_content = """When using React as an entirely client side SPA (ie no Node process on a server running React to create server side components), the default behaviour is that the entire compiled application has to be loaded by the browser. This can cause perceived slowness in the application as the whole script has to be loaded, parsed and executed before the UI starts to appear.

To allow applications to load and appear ready for interaction faster, React allows us to implement code-splitting. This allows the application to be loaded in seperate chunks, potentially improving the initial load time.

To code split, we mark some components to be lazy-loaded. This will mark them (and their children) as a boundry to split into a seperate file during the build. This file will then be loaded in a seperate HTTP request by React when the component(s) are required.

This does mean that when a so called lazy component is first requested, it may not be on the client. To imporve the UX whilst the file loads, React also provides a so-called Suspense boundary that allows you to render a fallback UI (such as a loading spinner) until the lazy component has been loaded and parsed.

"""
note_20_title = "HTTP Strict Transport Security"
note_20_content = """HTTP Strict Transport Security (HSTS) is a web security mechanism that forces browsers to interact with a website only over secure HTTPS connections. It is implemented by a server sending the Strict-Transport-Security header in its HTTPS response.

Once a browser receives this header, it caches the rule for the specified max-age. During this period, the browser will automatically upgrade any future requests to that domain from HTTP to HTTPS before they even leave the browser, preventing downgrade attacks and exposure of sensitive data. In practice, this means the potentially insecure HTTP request is never made.

HSTS mitigates protocol downgrade attacks and helps protect against issues like cookie hijacking over unencrypted channels. However, it only applies after the browser has seen the header once, unless the domain is on the global HSTS preload list that browsers implement.
"""
note_21_title = "Django Views"
note_21_content="""In Django, a view is any callable that the URL dispatcher invokes after matching a request path. It receives an HttpRequest and returns an HttpResponse (or subclass).

Common styles:
	•	Function-based views (FBVs): plain functions that take request and return a response; often paired with helpers (render, redirect) and decorators to implement common functionality.
	•	Class-based views (CBVs): classes providing reusable behavior. The as_view() method returns a callable that dispatches HTTP verbs to methods like get/post. CBVs compose well via mixins (e.g., LoginRequiredMixin, PermissionRequiredMixin).

Choosing between them:
	•	Simple views: if a suitable generic CBV exists (TemplateView, DetailView, ListView), use it; otherwise an FBV is fine.
	•	Moderate views (forms/CRUD/auth): CBVs are often clean and robust with minimal method overriding.
	•	Complex views: CBVs with custom mixins may still fit; if you’re overriding most behavior, consider if an FBV may be clearer.
"""
note_22_title = "TypeScript"
note_22_content="""JavaScript is a dynamically typed language, which means type errors are often only discovered at runtime. This can make it easy to introduce bugs, especially when handling user input in web applications.

TypeScript, developed by Microsoft, is an open-source superset of JavaScript that adds static typing. Developers can add type annotations, define interfaces, and describe the structure of data. The TypeScript compiler then checks code against these rules, catching errors before execution. This improves maintainability, reduces bugs, and enhances the developer experience, especially in large or complex projects.

TypeScript is primarily a development-time tool. Browsers and Node.js cannot execute TypeScript directly; types exist only during compilation and are stripped out afterwards. The TypeSxript source code must be transpiled into plain JavaScript using the TypeScript compiler or bundlers like Webpack or Vite. The output JavaScript is what runs in production.
"""