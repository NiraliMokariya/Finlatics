# %%
print("hello world!")


# %%
print("Good day")
# %% numeric
print(43)
# %%  concatenate
print("dumb" + "ashwin")

# %%
print('dumb', 'ashwin')
# %% concatenate strings and numbers
print("The result is", 52)
# %% printing multiple lines using print statement. to do it, we use three single quotes or three double quotes.
print('''hello,hru?
good,hbu?
fine. ''')
# %% incase of apostophe , we use escape that is \ to avoid confusion
Sentence = 'it\'s a beautiful day'
print(Sentence)
# %% incase of double quotes, we use \"
sentence="he said, \"python is amazing\""
print(sentence)
# %%\n = new line
print('twinle twinkle little star,\nhow i wonder what you are')

# %% \b = backspace one character
print('sup \b macha')

# %% (\\)backslash backslash = used to keep one backslash in string
print('hi \\hry')
# %% \t = tab character
print("hello\t world")

# %%  raw string
path= R"c:\Users\DELL\OneDrive\Desktop\RRESEARCH_METHODOLOGY"
print(path)
# %%  string formatting
name='raj'
name2='i\'m smart'
print('my name is {},and {}'.format(name,name2))

# %%  end parameter
print("one")
print("two")
# %% so to get rid of the extra space,we use end parameter which is set to "\n" by default
print('one',end=',')
print("two")
# %% sep parameter
print('apple','banana',"orange",sep='\\')

# %% using sep and end togeter in print()
print("fruits:" 'apple','banana',"orange",sep='|',end=' prices:')
print(23,29,80)

# %%numeric values using sep and end
num1=10
num2=20
num3=30
print("numbers:",num1,num2,num3,sep='|',end='..')
print("sum:",num1+num2+num3)

# %%
age="A+b"
print(age)
# %%
