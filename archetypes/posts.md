---
title: "{{ or (getenv "HUGO_POST_TITLE") (replace .File.ContentBaseName "-" " " | title) }}"
date: {{ .Date }}
draft: true
slug: "{{ .File.ContentBaseName }}"
categories: ["{{ or (getenv "HUGO_POST_CATEGORY") "Blog" }}"]
tags: []
summary: ""
---
