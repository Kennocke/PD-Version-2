# -*- coding: utf-8 -*-
from flask import render_template, redirect
from app import app
from app.forms import LoginForm
import requests, bs4, sys
import request

url = 'http://3dtoday.ru/blogs/news3dtoday/' # url для второй страницы
id_chat = -277981355

@app.route('/', methods=['GET', 'POST'])
def index():
	form = LoginForm()
	selected_users = []
	title_spis = []
	text_spis = []
	title_name = []
	test = []
	count = {"one","two","three","four","five"}
	count_id = {"one1","two2","three3","four4","five5"}
	r = requests.get(url)
	b = bs4.BeautifulSoup(r.text, "html.parser")
	for row in b.findAll(attrs={"class" : "post_list_item"}):
		for list in row.findAll(attrs={"class" : "title_bg"}):
			cols = "http://3dtoday.ru" + row.findAll('a')[0]["href"]
		item1 = row.findAll(attrs={"class" : "post_list_item_title"})
		item2 = row.findAll(attrs={"class" : "post_list_item_text"})
		title_spis.append(cols)
		text_spis.append(item2[0].text)
		title_name.append(item1[0].text)
		
	
	if form.validate_on_submit():
		selected_users = form.getlist("users")
		print(selected_users)
		return redirect('https://vk.com/audios71635260')		
	context = dict(pairs=zip(title_spis, text_spis, title_name, count, count_id))
	return render_template('index.html', title='Панель администратора', context = context, form = form, test = selected_users)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)