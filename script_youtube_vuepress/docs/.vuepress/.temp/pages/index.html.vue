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
<li>Setup Django</li>
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
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div><div class="line-number"></div></div></div><h1 id="vue" tabindex="-1"><a class="header-anchor" href="#vue"><span>Vue</span></a></h1>
<div class="language-cmd line-numbers-mode" data-highlighter="prismjs" data-ext="cmd" data-title="cmd"><pre v-pre><code><span class="line"></span></code></pre>
<div class="line-numbers" aria-hidden="true" style="counter-reset:line-number 0"></div></div></div></template>


