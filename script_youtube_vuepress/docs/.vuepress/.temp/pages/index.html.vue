<template><div><h1 id="vite-press" tabindex="-1"><a class="header-anchor" href="#vite-press"><span>Vite Press</span></a></h1>
<div class="language-cmd line-numbers-mode" data-highlighter="prismjs" data-ext="cmd" data-title="cmd"><pre v-pre><code><span class="line">npm init vuepress script_youtube_vuepress</span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><div class="language-cmd line-numbers-mode" data-highlighter="prismjs" data-ext="cmd" data-title="cmd"><pre v-pre><code><span class="line">cd script_youtube_vuepress</span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><div class="language-cmd line-numbers-mode" data-highlighter="prismjs" data-ext="cmd" data-title="cmd"><pre v-pre><code><span class="line">npm install -D sass-embedded</span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><div class="language-cmd line-numbers-mode" data-highlighter="prismjs" data-ext="cmd" data-title="cmd"><pre v-pre><code><span class="line">npm run docs:dev</span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><ul>
<li>Open Docs File 📁 &gt; Create File 📁</li>
</ul>
<div class="language-text line-numbers-mode" data-highlighter="prismjs" data-ext="text" data-title="text"><pre v-pre><code><span class="line">index.md</span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><h1 id="github" tabindex="-1"><a class="header-anchor" href="#github"><span>Github</span></a></h1>
<ul>
<li>Git Clone Project 📦</li>
</ul>
<div class="language-cmd line-numbers-mode" data-highlighter="prismjs" data-ext="cmd" data-title="cmd"><pre v-pre><code><span class="line">git clone https://github.com/LearnCodingEasy/script_youtube.git</span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><h1 id="license" tabindex="-1"><a class="header-anchor" href="#license"><span>LICENSE</span></a></h1>
<ul>
<li>Create File 📝 [ LICENSE ]</li>
</ul>
<div class="language-text line-numbers-mode" data-highlighter="prismjs" data-ext="text" data-title="text"><pre v-pre><code><span class="line">LICENSE</span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><div class="language-text line-numbers-mode" data-highlighter="prismjs" data-ext="text" data-title="text"><pre v-pre><code><span class="line">MIT License</span>
<span class="line">Copyright (c) 2024 Hossam Rashad</span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div></div></div><h1 id="django" tabindex="-1"><a class="header-anchor" href="#django"><span>Django</span></a></h1>
<ul>
<li>Create Virtual Environment</li>
</ul>
<div class="language-cmd line-numbers-mode" data-highlighter="prismjs" data-ext="cmd" data-title="cmd"><pre v-pre><code><span class="line">python -m venv script_youtube_virtual_environment</span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><ul>
<li>Activate Virtual Environment</li>
</ul>
<div class="language-cmd line-numbers-mode" data-highlighter="prismjs" data-ext="cmd" data-title="cmd"><pre v-pre><code><span class="line">script_youtube_virtual_environment\Scripts\activate</span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><ul>
<li>Install Django</li>
</ul>
<div class="language-cmd line-numbers-mode" data-highlighter="prismjs" data-ext="cmd" data-title="cmd"><pre v-pre><code><span class="line">pip install django</span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><ul>
<li>5 Install Django Libraries
[
1 - djangorestframework |
2 - djangorestframework-simplejwt |
3 - django-cors-headers |
4 - pillow
]</li>
</ul>
<div class="language-cmd line-numbers-mode" data-highlighter="prismjs" data-ext="cmd" data-title="cmd"><pre v-pre><code><span class="line">pip install djangorestframework djangorestframework-simplejwt django-cors-headers pillow</span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><ul>
<li>Create Django Project</li>
</ul>
<div class="language-cmd line-numbers-mode" data-highlighter="prismjs" data-ext="cmd" data-title="cmd"><pre v-pre><code><span class="line">django-admin startproject script_youtube_django</span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><ul>
<li>Create Django App</li>
</ul>
<div class="language-cmd line-numbers-mode" data-highlighter="prismjs" data-ext="cmd" data-title="cmd"><pre v-pre><code><span class="line">cd script_youtube_django</span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><div class="language-cmd line-numbers-mode" data-highlighter="prismjs" data-ext="cmd" data-title="cmd"><pre v-pre><code><span class="line">python manage.py startapp account</span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><ul>
<li>Setup Django File 📁 Settings</li>
</ul>
<div class="language-python line-numbers-mode" data-highlighter="prismjs" data-ext="py" data-title="py"><pre v-pre><code><span class="line"><span class="token comment"># Page [script_youtube/script_youtube_django/script_youtube_django/settings.py]</span></span>
<span class="line"></span>
<span class="line"><span class="token keyword">from</span> datetime <span class="token keyword">import</span> timedelta</span>
<span class="line">ALLOWED_HOSTS <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token punctuation">]</span></span>
<span class="line">WEBSITE_URL <span class="token operator">=</span> <span class="token string">"http://127.0.0.1:8000"</span></span>
<span class="line">AUTH_USER_MODEL <span class="token operator">=</span> <span class="token string">"account.User"</span></span>
<span class="line">SIMPLE_JWT <span class="token operator">=</span> <span class="token punctuation">{</span></span>
<span class="line">  <span class="token string">"ACCESS_TOKEN_LIFETIME"</span><span class="token punctuation">:</span> timedelta<span class="token punctuation">(</span>days<span class="token operator">=</span><span class="token number">30</span><span class="token punctuation">)</span><span class="token punctuation">,</span></span>
<span class="line">  <span class="token string">"REFRESH_TOKEN_LIFETIME"</span><span class="token punctuation">:</span> timedelta<span class="token punctuation">(</span>days<span class="token operator">=</span><span class="token number">180</span><span class="token punctuation">)</span><span class="token punctuation">,</span></span>
<span class="line">  <span class="token string">"ROTATE_REFRESH_TOKENS"</span><span class="token punctuation">:</span> <span class="token boolean">False</span><span class="token punctuation">,</span></span>
<span class="line"><span class="token punctuation">}</span></span>
<span class="line"></span>
<span class="line">REST_FRAMEWORK <span class="token operator">=</span> <span class="token punctuation">{</span></span>
<span class="line">  <span class="token string">"DEFAULT_AUTHENTICATION_CLASSES"</span><span class="token punctuation">:</span> <span class="token punctuation">(</span></span>
<span class="line">      <span class="token string">"rest_framework_simplejwt.authentication.JWTAuthentication"</span><span class="token punctuation">,</span></span>
<span class="line">  <span class="token punctuation">)</span><span class="token punctuation">,</span></span>
<span class="line">  <span class="token string">"DEFAULT_PERMISSION_CLASSES"</span><span class="token punctuation">:</span> <span class="token punctuation">(</span><span class="token string">"rest_framework.permissions.IsAuthenticated"</span><span class="token punctuation">,</span><span class="token punctuation">)</span><span class="token punctuation">,</span></span>
<span class="line"><span class="token punctuation">}</span></span>
<span class="line"></span>
<span class="line">CORS_ALLOWED_ORIGINS <span class="token operator">=</span> <span class="token punctuation">[</span></span>
<span class="line">  <span class="token string">"http://localhost:5173"</span><span class="token punctuation">,</span></span>
<span class="line">  <span class="token string">"http://localhost:5174"</span><span class="token punctuation">,</span></span>
<span class="line"><span class="token punctuation">]</span></span>
<span class="line"></span>
<span class="line">CSRF_TRUSTED_ORIGINS <span class="token operator">=</span> <span class="token punctuation">[</span></span>
<span class="line">  <span class="token string">"http://localhost:5173"</span><span class="token punctuation">,</span></span>
<span class="line">  <span class="token string">"http://localhost:5174"</span><span class="token punctuation">,</span></span>
<span class="line"><span class="token punctuation">]</span></span>
<span class="line"></span>
<span class="line">INSTALLED_APPS <span class="token operator">=</span> <span class="token punctuation">[</span></span>
<span class="line">    <span class="token comment"># ...</span></span>
<span class="line">    <span class="token comment"># Apps</span></span>
<span class="line">    <span class="token string">"account"</span><span class="token punctuation">,</span></span>
<span class="line">    <span class="token comment"># Libraries</span></span>
<span class="line">    <span class="token string">"rest_framework"</span><span class="token punctuation">,</span></span>
<span class="line">    <span class="token string">"rest_framework_simplejwt"</span><span class="token punctuation">,</span></span>
<span class="line">    <span class="token string">"corsheaders"</span><span class="token punctuation">,</span></span>
<span class="line"><span class="token punctuation">]</span></span>
<span class="line"></span>
<span class="line">MIDDLEWARE <span class="token operator">=</span> <span class="token punctuation">[</span></span>
<span class="line">    <span class="token comment"># ...</span></span>
<span class="line">    <span class="token string">"corsheaders.middleware.CorsMiddleware"</span><span class="token punctuation">,</span></span>
<span class="line">    <span class="token comment"># ...</span></span>
<span class="line"><span class="token punctuation">]</span></span>
<span class="line"></span>
<span class="line">MEDIA_URL <span class="token operator">=</span> <span class="token string">"media/"</span></span>
<span class="line">MEDIA_ROOT <span class="token operator">=</span> BASE_DIR <span class="token operator">/</span> <span class="token string">"media"</span></span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><ul>
<li>Setup Django App 📦 Account</li>
</ul>
<div class="language-python line-numbers-mode" data-highlighter="prismjs" data-ext="py" data-title="py"><pre v-pre><code><span class="line"><span class="token comment"># Page [ script_youtube/script_youtube_django/account/models.py ]</span></span>
<span class="line"></span>
<span class="line"><span class="token keyword">import</span> uuid</span>
<span class="line"><span class="token keyword">from</span> django<span class="token punctuation">.</span>conf <span class="token keyword">import</span> settings</span>
<span class="line"><span class="token keyword">from</span> django<span class="token punctuation">.</span>contrib<span class="token punctuation">.</span>auth<span class="token punctuation">.</span>models <span class="token keyword">import</span> AbstractBaseUser<span class="token punctuation">,</span> PermissionsMixin<span class="token punctuation">,</span> UserManager</span>
<span class="line"><span class="token keyword">from</span> django<span class="token punctuation">.</span>db <span class="token keyword">import</span> models</span>
<span class="line"><span class="token keyword">from</span> django<span class="token punctuation">.</span>utils <span class="token keyword">import</span> timezone</span>
<span class="line"></span>
<span class="line"><span class="token keyword">class</span> <span class="token class-name">CustomUserManager</span><span class="token punctuation">(</span>UserManager<span class="token punctuation">)</span><span class="token punctuation">:</span></span>
<span class="line">    <span class="token keyword">def</span> <span class="token function">_create_user</span><span class="token punctuation">(</span>self<span class="token punctuation">,</span> name<span class="token punctuation">,</span> email<span class="token punctuation">,</span> password<span class="token punctuation">,</span> <span class="token operator">**</span>extra_fields<span class="token punctuation">)</span><span class="token punctuation">:</span></span>
<span class="line">        <span class="token keyword">if</span> <span class="token keyword">not</span> email<span class="token punctuation">:</span></span>
<span class="line">            <span class="token keyword">raise</span> ValueError<span class="token punctuation">(</span><span class="token string">"You have not provided a valid e-mail address"</span><span class="token punctuation">)</span></span>
<span class="line">        email <span class="token operator">=</span> self<span class="token punctuation">.</span>normalize_email<span class="token punctuation">(</span>email<span class="token punctuation">)</span></span>
<span class="line">        user <span class="token operator">=</span> self<span class="token punctuation">.</span>model<span class="token punctuation">(</span>email<span class="token operator">=</span>email<span class="token punctuation">,</span> name<span class="token operator">=</span>name<span class="token punctuation">,</span> <span class="token operator">**</span>extra_fields<span class="token punctuation">)</span></span>
<span class="line">        user<span class="token punctuation">.</span>set_password<span class="token punctuation">(</span>password<span class="token punctuation">)</span></span>
<span class="line">        user<span class="token punctuation">.</span>save<span class="token punctuation">(</span>using<span class="token operator">=</span>self<span class="token punctuation">.</span>_db<span class="token punctuation">)</span></span>
<span class="line">        <span class="token keyword">return</span> user</span>
<span class="line"></span>
<span class="line">    <span class="token keyword">def</span> <span class="token function">create_user</span><span class="token punctuation">(</span>self<span class="token punctuation">,</span> name<span class="token operator">=</span><span class="token boolean">None</span><span class="token punctuation">,</span> email<span class="token operator">=</span><span class="token boolean">None</span><span class="token punctuation">,</span> password<span class="token operator">=</span><span class="token boolean">None</span><span class="token punctuation">,</span> <span class="token operator">**</span>extra_fields<span class="token punctuation">)</span><span class="token punctuation">:</span></span>
<span class="line">        extra_fields<span class="token punctuation">.</span>setdefault<span class="token punctuation">(</span><span class="token string">"is_staff"</span><span class="token punctuation">,</span> <span class="token boolean">False</span><span class="token punctuation">)</span></span>
<span class="line">        extra_fields<span class="token punctuation">.</span>setdefault<span class="token punctuation">(</span><span class="token string">"is_superuser"</span><span class="token punctuation">,</span> <span class="token boolean">False</span><span class="token punctuation">)</span></span>
<span class="line">        <span class="token keyword">return</span> self<span class="token punctuation">.</span>_create_user<span class="token punctuation">(</span>name<span class="token punctuation">,</span> email<span class="token punctuation">,</span> password<span class="token punctuation">,</span> <span class="token operator">**</span>extra_fields<span class="token punctuation">)</span></span>
<span class="line"></span>
<span class="line">    <span class="token keyword">def</span> <span class="token function">create_superuser</span><span class="token punctuation">(</span>self<span class="token punctuation">,</span> name<span class="token operator">=</span><span class="token boolean">None</span><span class="token punctuation">,</span> email<span class="token operator">=</span><span class="token boolean">None</span><span class="token punctuation">,</span> password<span class="token operator">=</span><span class="token boolean">None</span><span class="token punctuation">,</span> <span class="token operator">**</span>extra_fields<span class="token punctuation">)</span><span class="token punctuation">:</span></span>
<span class="line">        extra_fields<span class="token punctuation">.</span>setdefault<span class="token punctuation">(</span><span class="token string">"is_staff"</span><span class="token punctuation">,</span> <span class="token boolean">True</span><span class="token punctuation">)</span></span>
<span class="line">        extra_fields<span class="token punctuation">.</span>setdefault<span class="token punctuation">(</span><span class="token string">"is_superuser"</span><span class="token punctuation">,</span> <span class="token boolean">True</span><span class="token punctuation">)</span></span>
<span class="line">        <span class="token keyword">return</span> self<span class="token punctuation">.</span>_create_user<span class="token punctuation">(</span>name<span class="token punctuation">,</span> email<span class="token punctuation">,</span> password<span class="token punctuation">,</span> <span class="token operator">**</span>extra_fields<span class="token punctuation">)</span></span>
<span class="line"></span>
<span class="line"><span class="token keyword">class</span> <span class="token class-name">User</span><span class="token punctuation">(</span>AbstractBaseUser<span class="token punctuation">,</span> PermissionsMixin<span class="token punctuation">)</span><span class="token punctuation">:</span></span>
<span class="line">    <span class="token builtin">id</span> <span class="token operator">=</span> models<span class="token punctuation">.</span>UUIDField<span class="token punctuation">(</span>primary_key<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">,</span> default<span class="token operator">=</span>uuid<span class="token punctuation">.</span>uuid4<span class="token punctuation">,</span> editable<span class="token operator">=</span><span class="token boolean">False</span><span class="token punctuation">)</span></span>
<span class="line">          </span>
<span class="line">    name <span class="token operator">=</span> models<span class="token punctuation">.</span>CharField<span class="token punctuation">(</span>max_length<span class="token operator">=</span><span class="token number">255</span><span class="token punctuation">,</span> blank<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">,</span> default<span class="token operator">=</span><span class="token string">""</span><span class="token punctuation">)</span></span>
<span class="line">    surname <span class="token operator">=</span> models<span class="token punctuation">.</span>CharField<span class="token punctuation">(</span>max_length<span class="token operator">=</span><span class="token number">255</span><span class="token punctuation">,</span> blank<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">,</span> default<span class="token operator">=</span><span class="token string">""</span><span class="token punctuation">)</span></span>
<span class="line">    email <span class="token operator">=</span> models<span class="token punctuation">.</span>EmailField<span class="token punctuation">(</span>unique<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">)</span></span>
<span class="line">    date_of_birth <span class="token operator">=</span> models<span class="token punctuation">.</span>DateField<span class="token punctuation">(</span>default<span class="token operator">=</span>timezone<span class="token punctuation">.</span>now<span class="token punctuation">)</span></span>
<span class="line">    gender <span class="token operator">=</span> models<span class="token punctuation">.</span>CharField<span class="token punctuation">(</span>max_length<span class="token operator">=</span><span class="token number">15</span><span class="token punctuation">,</span> blank<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">,</span> null<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">)</span></span>
<span class="line">    avatar <span class="token operator">=</span> models<span class="token punctuation">.</span>ImageField<span class="token punctuation">(</span>upload_to<span class="token operator">=</span><span class="token string">"avatars"</span><span class="token punctuation">,</span> blank<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">,</span> null<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">)</span></span>
<span class="line">    cover <span class="token operator">=</span> models<span class="token punctuation">.</span>ImageField<span class="token punctuation">(</span>upload_to<span class="token operator">=</span><span class="token string">"covers"</span><span class="token punctuation">,</span> blank<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">,</span> null<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">)</span></span>
<span class="line">        </span>
<span class="line">    is_active <span class="token operator">=</span> models<span class="token punctuation">.</span>BooleanField<span class="token punctuation">(</span>default<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">)</span></span>
<span class="line">    is_superuser <span class="token operator">=</span> models<span class="token punctuation">.</span>BooleanField<span class="token punctuation">(</span>default<span class="token operator">=</span><span class="token boolean">False</span><span class="token punctuation">)</span></span>
<span class="line">    is_staff <span class="token operator">=</span> models<span class="token punctuation">.</span>BooleanField<span class="token punctuation">(</span>default<span class="token operator">=</span><span class="token boolean">False</span><span class="token punctuation">)</span></span>
<span class="line">        </span>
<span class="line">    date_joined <span class="token operator">=</span> models<span class="token punctuation">.</span>DateTimeField<span class="token punctuation">(</span>default<span class="token operator">=</span>timezone<span class="token punctuation">.</span>now<span class="token punctuation">)</span></span>
<span class="line">    last_login <span class="token operator">=</span> models<span class="token punctuation">.</span>DateTimeField<span class="token punctuation">(</span>blank<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">,</span> null<span class="token operator">=</span><span class="token boolean">True</span><span class="token punctuation">)</span></span>
<span class="line">        </span>
<span class="line">    objects <span class="token operator">=</span> CustomUserManager<span class="token punctuation">(</span><span class="token punctuation">)</span></span>
<span class="line">        </span>
<span class="line">    USERNAME_FIELD <span class="token operator">=</span> <span class="token string">"email"</span></span>
<span class="line">    EMAIL_FIELD <span class="token operator">=</span> <span class="token string">"email"</span></span>
<span class="line">    REQUIRED_FIELDS <span class="token operator">=</span> <span class="token punctuation">[</span><span class="token punctuation">]</span></span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><ul>
<li>Create Page 📝 [ serializers.py ] Inside App Account</li>
</ul>
<div class="language-text line-numbers-mode" data-highlighter="prismjs" data-ext="text" data-title="text"><pre v-pre><code><span class="line">serializers.py</span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><div class="language-python line-numbers-mode" data-highlighter="prismjs" data-ext="py" data-title="py"><pre v-pre><code><span class="line"><span class="token comment"># Page [ script_youtube/script_youtube_django/account/serializers.py ]</span></span>
<span class="line"><span class="token keyword">from</span> rest_framework <span class="token keyword">import</span> serializers</span>
<span class="line"><span class="token keyword">from</span> <span class="token punctuation">.</span>models <span class="token keyword">import</span> User</span>
<span class="line"><span class="token keyword">class</span> <span class="token class-name">UserSerializer</span><span class="token punctuation">(</span>serializers<span class="token punctuation">.</span>ModelSerializer<span class="token punctuation">)</span><span class="token punctuation">:</span></span>
<span class="line">  <span class="token keyword">class</span> <span class="token class-name">Meta</span><span class="token punctuation">:</span></span>
<span class="line">    model <span class="token operator">=</span> User</span>
<span class="line">    fields <span class="token operator">=</span> <span class="token punctuation">(</span></span>
<span class="line">      <span class="token string">"id"</span><span class="token punctuation">,</span></span>
<span class="line">      <span class="token string">"name"</span><span class="token punctuation">,</span></span>
<span class="line">      <span class="token string">"surname"</span><span class="token punctuation">,</span></span>
<span class="line">      <span class="token string">"email"</span><span class="token punctuation">,</span></span>
<span class="line">      <span class="token string">"date_of_birth"</span><span class="token punctuation">,</span></span>
<span class="line">      <span class="token string">"gender"</span><span class="token punctuation">,</span></span>
<span class="line">    <span class="token punctuation">)</span></span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><ul>
<li>Create Page 📝[ forms.py ] Inside App Account</li>
</ul>
<div class="language-text line-numbers-mode" data-highlighter="prismjs" data-ext="text" data-title="text"><pre v-pre><code><span class="line">forms.py</span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><div class="language-python line-numbers-mode" data-highlighter="prismjs" data-ext="py" data-title="py"><pre v-pre><code><span class="line"><span class="token comment"># Page [ script_youtube/script_youtube_django/account/forms.py ]</span></span>
<span class="line"></span>
<span class="line"><span class="token keyword">from</span> django<span class="token punctuation">.</span>contrib<span class="token punctuation">.</span>auth<span class="token punctuation">.</span>forms <span class="token keyword">import</span> UserCreationForm</span>
<span class="line"><span class="token keyword">from</span> django <span class="token keyword">import</span> forms</span>
<span class="line"><span class="token keyword">from</span> <span class="token punctuation">.</span>models <span class="token keyword">import</span> User</span>
<span class="line"><span class="token keyword">class</span> <span class="token class-name">SignupForm</span><span class="token punctuation">(</span>UserCreationForm<span class="token punctuation">)</span><span class="token punctuation">:</span></span>
<span class="line">    <span class="token keyword">class</span> <span class="token class-name">Meta</span><span class="token punctuation">:</span></span>
<span class="line">        model <span class="token operator">=</span> User</span>
<span class="line">        fields <span class="token operator">=</span> <span class="token punctuation">(</span></span>
<span class="line">            <span class="token string">"name"</span><span class="token punctuation">,</span></span>
<span class="line">            <span class="token string">"surname"</span><span class="token punctuation">,</span></span>
<span class="line">            <span class="token string">"email"</span><span class="token punctuation">,</span></span>
<span class="line">            <span class="token string">"date_of_birth"</span><span class="token punctuation">,</span></span>
<span class="line">            <span class="token string">"gender"</span><span class="token punctuation">,</span></span>
<span class="line">            <span class="token string">"password1"</span><span class="token punctuation">,</span></span>
<span class="line">            <span class="token string">"password2"</span><span class="token punctuation">,</span></span>
<span class="line">        <span class="token punctuation">)</span></span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><ul>
<li>Create Page 📝 [ api.py ] Inside App Account</li>
</ul>
<div class="language-text line-numbers-mode" data-highlighter="prismjs" data-ext="text" data-title="text"><pre v-pre><code><span class="line">api.py</span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><div class="language-python line-numbers-mode" data-highlighter="prismjs" data-ext="py" data-title="py"><pre v-pre><code><span class="line"><span class="token comment"># Page [ script_youtube/script_youtube_django/account/api.py ]</span></span>
<span class="line"></span>
<span class="line"><span class="token keyword">from</span> django<span class="token punctuation">.</span>conf <span class="token keyword">import</span> settings</span>
<span class="line"><span class="token keyword">from</span> django<span class="token punctuation">.</span>contrib<span class="token punctuation">.</span>auth<span class="token punctuation">.</span>forms <span class="token keyword">import</span> PasswordChangeForm</span>
<span class="line"><span class="token keyword">from</span> django<span class="token punctuation">.</span>core<span class="token punctuation">.</span>mail <span class="token keyword">import</span> send_mail</span>
<span class="line"><span class="token keyword">from</span> django<span class="token punctuation">.</span>http <span class="token keyword">import</span> JsonResponse</span>
<span class="line"><span class="token keyword">from</span> rest_framework<span class="token punctuation">.</span>decorators <span class="token keyword">import</span> <span class="token punctuation">(</span></span>
<span class="line">    api_view<span class="token punctuation">,</span></span>
<span class="line">    authentication_classes<span class="token punctuation">,</span></span>
<span class="line">    permission_classes<span class="token punctuation">,</span></span>
<span class="line"><span class="token punctuation">)</span></span>
<span class="line"><span class="token keyword">from</span> <span class="token punctuation">.</span>forms <span class="token keyword">import</span> SignupForm</span>
<span class="line"><span class="token keyword">from</span> <span class="token punctuation">.</span>models <span class="token keyword">import</span> User</span>
<span class="line"><span class="token keyword">from</span> <span class="token punctuation">.</span>serializers <span class="token keyword">import</span> UserSerializer</span>
<span class="line"></span>
<span class="line"><span class="token decorator annotation punctuation">@api_view</span><span class="token punctuation">(</span><span class="token punctuation">[</span><span class="token string">"POST"</span><span class="token punctuation">]</span><span class="token punctuation">)</span></span>
<span class="line"><span class="token decorator annotation punctuation">@authentication_classes</span><span class="token punctuation">(</span><span class="token punctuation">[</span><span class="token punctuation">]</span><span class="token punctuation">)</span></span>
<span class="line"><span class="token decorator annotation punctuation">@permission_classes</span><span class="token punctuation">(</span><span class="token punctuation">[</span><span class="token punctuation">]</span><span class="token punctuation">)</span></span>
<span class="line"><span class="token keyword">def</span> <span class="token function">signup</span><span class="token punctuation">(</span>request<span class="token punctuation">)</span><span class="token punctuation">:</span></span>
<span class="line"></span>
<span class="line">  data <span class="token operator">=</span> request<span class="token punctuation">.</span>data</span>
<span class="line">  message <span class="token operator">=</span> <span class="token string">"success"</span></span>
<span class="line"></span>
<span class="line">  form <span class="token operator">=</span> SignupForm<span class="token punctuation">(</span></span>
<span class="line">    <span class="token punctuation">{</span></span>
<span class="line">      <span class="token string">"name"</span><span class="token punctuation">:</span> data<span class="token punctuation">.</span>get<span class="token punctuation">(</span><span class="token string">"name"</span><span class="token punctuation">)</span><span class="token punctuation">,</span></span>
<span class="line">      <span class="token string">"surname"</span><span class="token punctuation">:</span> data<span class="token punctuation">.</span>get<span class="token punctuation">(</span><span class="token string">"surname"</span><span class="token punctuation">)</span><span class="token punctuation">,</span></span>
<span class="line">      <span class="token string">"email"</span><span class="token punctuation">:</span> data<span class="token punctuation">.</span>get<span class="token punctuation">(</span><span class="token string">"email"</span><span class="token punctuation">)</span><span class="token punctuation">,</span></span>
<span class="line">      <span class="token string">"date_of_birth"</span><span class="token punctuation">:</span> data<span class="token punctuation">.</span>get<span class="token punctuation">(</span><span class="token string">"date_of_birth"</span><span class="token punctuation">)</span><span class="token punctuation">,</span></span>
<span class="line">      <span class="token string">"gender"</span><span class="token punctuation">:</span> data<span class="token punctuation">.</span>get<span class="token punctuation">(</span><span class="token string">"gender"</span><span class="token punctuation">)</span><span class="token punctuation">,</span></span>
<span class="line">      <span class="token string">"password1"</span><span class="token punctuation">:</span> data<span class="token punctuation">.</span>get<span class="token punctuation">(</span><span class="token string">"password1"</span><span class="token punctuation">)</span><span class="token punctuation">,</span></span>
<span class="line">      <span class="token string">"password2"</span><span class="token punctuation">:</span> data<span class="token punctuation">.</span>get<span class="token punctuation">(</span><span class="token string">"password2"</span><span class="token punctuation">)</span><span class="token punctuation">,</span></span>
<span class="line">    <span class="token punctuation">}</span></span>
<span class="line">  <span class="token punctuation">)</span></span>
<span class="line"></span>
<span class="line">  <span class="token keyword">if</span> form<span class="token punctuation">.</span>is_valid<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">:</span></span>
<span class="line">    user <span class="token operator">=</span> form<span class="token punctuation">.</span>save<span class="token punctuation">(</span><span class="token punctuation">)</span></span>
<span class="line">    user<span class="token punctuation">.</span>is_active <span class="token operator">=</span> <span class="token boolean">False</span></span>
<span class="line">    user<span class="token punctuation">.</span>save<span class="token punctuation">(</span><span class="token punctuation">)</span></span>
<span class="line"></span>
<span class="line">    <span class="token keyword">return</span> JsonResponse<span class="token punctuation">(</span><span class="token punctuation">{</span><span class="token string">"message"</span><span class="token punctuation">:</span> message<span class="token punctuation">,</span> <span class="token string">"email_sent"</span><span class="token punctuation">:</span> <span class="token boolean">True</span><span class="token punctuation">}</span><span class="token punctuation">,</span> safe<span class="token operator">=</span><span class="token boolean">False</span><span class="token punctuation">)</span></span>
<span class="line">  <span class="token keyword">else</span><span class="token punctuation">:</span></span>
<span class="line">    message <span class="token operator">=</span> form<span class="token punctuation">.</span>errors<span class="token punctuation">.</span>as_json<span class="token punctuation">(</span><span class="token punctuation">)</span></span>
<span class="line"></span>
<span class="line">  <span class="token keyword">print</span><span class="token punctuation">(</span>message<span class="token punctuation">)</span></span>
<span class="line"></span>
<span class="line">  <span class="token keyword">return</span> JsonResponse<span class="token punctuation">(</span><span class="token punctuation">{</span><span class="token string">"message"</span><span class="token punctuation">:</span> message<span class="token punctuation">}</span><span class="token punctuation">,</span> safe<span class="token operator">=</span><span class="token boolean">False</span><span class="token punctuation">)</span></span>
<span class="line"></span>
<span class="line"></span>
<span class="line"><span class="token decorator annotation punctuation">@api_view</span><span class="token punctuation">(</span><span class="token punctuation">[</span><span class="token string">"GET"</span><span class="token punctuation">]</span><span class="token punctuation">)</span></span>
<span class="line"><span class="token keyword">def</span> <span class="token function">me</span><span class="token punctuation">(</span>request<span class="token punctuation">)</span><span class="token punctuation">:</span></span>
<span class="line">  <span class="token keyword">return</span> JsonResponse<span class="token punctuation">(</span></span>
<span class="line">    <span class="token punctuation">{</span></span>
<span class="line">      <span class="token string">"id"</span><span class="token punctuation">:</span> request<span class="token punctuation">.</span>user<span class="token punctuation">.</span><span class="token builtin">id</span><span class="token punctuation">,</span></span>
<span class="line">      <span class="token string">"name"</span><span class="token punctuation">:</span> request<span class="token punctuation">.</span>user<span class="token punctuation">.</span>name<span class="token punctuation">,</span></span>
<span class="line">      <span class="token string">"surname"</span><span class="token punctuation">:</span> request<span class="token punctuation">.</span>user<span class="token punctuation">.</span>surname<span class="token punctuation">,</span></span>
<span class="line">      <span class="token string">"email"</span><span class="token punctuation">:</span> request<span class="token punctuation">.</span>user<span class="token punctuation">.</span>email<span class="token punctuation">,</span></span>
<span class="line">      <span class="token string">"date_of_birth"</span><span class="token punctuation">:</span> request<span class="token punctuation">.</span>user<span class="token punctuation">.</span>date_of_birth<span class="token punctuation">,</span></span>
<span class="line">      <span class="token string">"gender"</span><span class="token punctuation">:</span> request<span class="token punctuation">.</span>user<span class="token punctuation">.</span>gender<span class="token punctuation">,</span></span>
<span class="line">    <span class="token punctuation">}</span></span>
<span class="line">  <span class="token punctuation">)</span></span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><ul>
<li>Create Page 📝[ urls.py ] Inside App Account</li>
</ul>
<div class="language-text line-numbers-mode" data-highlighter="prismjs" data-ext="text" data-title="text"><pre v-pre><code><span class="line">urls.py</span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><div class="language-python line-numbers-mode" data-highlighter="prismjs" data-ext="py" data-title="py"><pre v-pre><code><span class="line"><span class="token comment"># Page [ script_youtube/script_youtube_django/account/urls.py ]</span></span>
<span class="line"><span class="token keyword">from</span> django<span class="token punctuation">.</span>urls <span class="token keyword">import</span> path</span>
<span class="line"><span class="token keyword">from</span> rest_framework_simplejwt<span class="token punctuation">.</span>views <span class="token keyword">import</span> TokenObtainPairView<span class="token punctuation">,</span> TokenRefreshView</span>
<span class="line"></span>
<span class="line"><span class="token keyword">from</span> <span class="token punctuation">.</span> <span class="token keyword">import</span> api</span>
<span class="line"></span>
<span class="line">urlpatterns <span class="token operator">=</span> <span class="token punctuation">[</span></span>
<span class="line">    path<span class="token punctuation">(</span><span class="token string">"me/"</span><span class="token punctuation">,</span> api<span class="token punctuation">.</span>me<span class="token punctuation">,</span> name<span class="token operator">=</span><span class="token string">"me"</span><span class="token punctuation">)</span><span class="token punctuation">,</span></span>
<span class="line">    path<span class="token punctuation">(</span><span class="token string">"signup/"</span><span class="token punctuation">,</span> api<span class="token punctuation">.</span>signup<span class="token punctuation">,</span> name<span class="token operator">=</span><span class="token string">"signup"</span><span class="token punctuation">)</span><span class="token punctuation">,</span></span>
<span class="line">    path<span class="token punctuation">(</span><span class="token string">"login/"</span><span class="token punctuation">,</span> TokenObtainPairView<span class="token punctuation">.</span>as_view<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">,</span> name<span class="token operator">=</span><span class="token string">"token_obtain"</span><span class="token punctuation">)</span><span class="token punctuation">,</span></span>
<span class="line">    path<span class="token punctuation">(</span><span class="token string">"refresh/"</span><span class="token punctuation">,</span> TokenRefreshView<span class="token punctuation">.</span>as_view<span class="token punctuation">(</span><span class="token punctuation">)</span><span class="token punctuation">,</span> name<span class="token operator">=</span><span class="token string">"token_refresh"</span><span class="token punctuation">)</span><span class="token punctuation">,</span></span>
<span class="line"><span class="token punctuation">]</span></span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><ul>
<li>Setup Page 📝 [ url.py ] Inside script_youtube_django</li>
</ul>
<div class="language-python line-numbers-mode" data-highlighter="prismjs" data-ext="py" data-title="py"><pre v-pre><code><span class="line"><span class="token comment"># Page [ script_youtube/script_youtube_django/script_youtube_django/urls.py ]</span></span>
<span class="line"></span>
<span class="line"><span class="token keyword">from</span> django<span class="token punctuation">.</span>contrib <span class="token keyword">import</span> admin</span>
<span class="line"><span class="token keyword">from</span> django<span class="token punctuation">.</span>urls <span class="token keyword">import</span> path<span class="token punctuation">,</span> include</span>
<span class="line"><span class="token keyword">from</span> django<span class="token punctuation">.</span>conf <span class="token keyword">import</span> settings</span>
<span class="line"><span class="token keyword">from</span> django<span class="token punctuation">.</span>conf<span class="token punctuation">.</span>urls<span class="token punctuation">.</span>static <span class="token keyword">import</span> static</span>
<span class="line"></span>
<span class="line">urlpatterns <span class="token operator">=</span> <span class="token punctuation">[</span></span>
<span class="line">    path<span class="token punctuation">(</span><span class="token string">"api/"</span><span class="token punctuation">,</span> include<span class="token punctuation">(</span><span class="token string">"account.urls"</span><span class="token punctuation">)</span><span class="token punctuation">)</span><span class="token punctuation">,</span></span>
<span class="line">    path<span class="token punctuation">(</span><span class="token string">"admin/"</span><span class="token punctuation">,</span> admin<span class="token punctuation">.</span>site<span class="token punctuation">.</span>urls<span class="token punctuation">)</span><span class="token punctuation">,</span></span>
<span class="line"><span class="token punctuation">]</span> <span class="token operator">+</span> static<span class="token punctuation">(</span>settings<span class="token punctuation">.</span>MEDIA_URL<span class="token punctuation">,</span> document_root<span class="token operator">=</span>settings<span class="token punctuation">.</span>MEDIA_ROOT<span class="token punctuation">)</span></span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><ul>
<li>🛠️ Modifications To Models File</li>
</ul>
<div class="language-cmd line-numbers-mode" data-highlighter="prismjs" data-ext="cmd" data-title="cmd"><pre v-pre><code><span class="line">python manage.py makemigrations</span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><ul>
<li>🛠️ Modifications To The Database</li>
</ul>
<div class="language-cmd line-numbers-mode" data-highlighter="prismjs" data-ext="cmd" data-title="cmd"><pre v-pre><code><span class="line">python manage.py migrate</span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><ul>
<li>🚀 Try The Project On Your Device</li>
</ul>
<div class="language-cmd line-numbers-mode" data-highlighter="prismjs" data-ext="cmd" data-title="cmd"><pre v-pre><code><span class="line">python manage.py runserver</span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><h1 id="vue" tabindex="-1"><a class="header-anchor" href="#vue"><span>Vue</span></a></h1>
<ul>
<li>Create Vue Project</li>
</ul>
<div class="language-cmd line-numbers-mode" data-highlighter="prismjs" data-ext="cmd" data-title="cmd"><pre v-pre><code><span class="line">npm create vue@latest</span>
<span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div></div></div><ul>
<li>11 Choose Vite [ Project name &amp; Select a framework ]
√ Project name: ... facebook_vue
√ Add TypeScript? ... No / Yes
√ Add JSX Support? ... No / Yes
√ Add Vue Router for Single Page Application development? ... No / Yes
√ Add Pinia for state management? ... No / Yes
√ Add Vitest for Unit Testing? ... No / Yes
√ Add an End-to-End Testing Solution? » No
√ Add ESLint for code quality? ... No / Yes
√ Add Prettier for code formatting? ... No / Yes
√ Add Vue DevTools 7 extension for debugging? (experimental) ... No / Yes</li>
</ul>
<p>Scaffolding project in E:\Projects\Facebook\facebook_vue...</p>
<p>Done. Now run:
cd facebook_vue
npm install
npm run format
npm run dev</p>
<div class="language-text line-numbers-mode" data-highlighter="prismjs" data-ext="text" data-title="text"><pre v-pre><code><span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"></div></div></div></template>


