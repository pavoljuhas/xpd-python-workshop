# Reading #

  * [Python Tutorial](http://docs.python.org/2/tutorial/)
  * Mercurial [Quick Start Guide](http://mercurial.selenic.com/quickstart/) and [Tutorial](http://hginit.com/)

# Software #

The workshop attendees should have their own computer with
the following software installed:

  1. Python 2.7
  1. IPython
  1. NumPy
  1. MatplotLib
  1. Mercurial command line tool

The software should be available for use from the command line so that "python", "ipython",
and "hg" can be run from any directory in the terminal (Command Prompt on Windows).  The preferred operating system is Linux or Mac, Windows can be used as well.

## Linux Notes ##

On Ubuntu Linux or other Debian based distribution the required software can be all installed with
```
sudo apt-get install \
    python ipython python-numpy python-matplotlib \
    mercurial
```

## Mac OSX Notes ##

On Mac OSX the easiest way might be to install macports from http://www.macports.org/ and then execute
in the terminal
```
sudo port install \
    python27 py27-ipython py27-numpy py27-matplotlib \
    mercurial
sudo port select --set python python27
```

Another option is to use the [Enthought Python](https://www.enthought.com/products/epd/), which already includes all the required Python packages.  The command-line mercurial client can be obtained from http://mercurial.selenic.com/.

## Windows Notes ##

On Windows the best bet is to use either [Enthought Python](https://www.enthought.com/products/epd/) or
[PythonXY](https://code.google.com/p/pythonxy/) that come with the required set of Python packages.
Use the command line mercurial client from http://mercurial.selenic.com/downloads/ page.  Although there are GUI driven mercurial clients like tortoise, it is preferable to use the command-line version to have a uniform way of interacting with the software.

## Text Editor ##

Python programs are simple text files where the text indentation is essential for the meaning and syntactical correctness of the code.  It is preferred to use a text editor with some features for editing source codes, for example, automatic indentation of the new lines.
Using TAB characters in the code may cause inconsistent code indentation,
therefore it is best to avoid them altogether and configure the editor to
insert 4 spaces instead of a TAB.  Another important setting is to always use
Unix line ends in the source code, where the newline is a single character rather than a carriage-return + newline pair as happens for Windows text files.

Here are some tips for good free text editors taken from the
[Google Python Class](https://developers.google.com/edu/python/).

  * Windows Notepad++ -- Tabs: _Settings --> Preferences --> Edit Components --> Tab settings_, and _Settings --> Preferences --> MISC_ for auto-indent. Line endings: _Format --> Convert_, set to Unix.

  * JEdit (any OS) -- Line endings: Little 'U' 'W' 'M' on status bar, set it to 'U' (i.e. Unix line-endings)

  * Windows Notepad or Wordpad -- **do not use**

  * Mac TextWrangler -- Tabs: Preference button at the top of the window, check Auto Expand Tabs. Can set the default in Defaults > Auto-Expand Tabs and Auto-indent. Line endings: little control at the bottom of each window, set it to Unix

  * Mac TextEdit -- do not use

  * Unix gedit -- Tabs: Edit --> Preferences --> Editor - set tab width to 4, check _Insert spaces instead of tabs_ and _Enable automatic indentation_.

  * Unix pico or nano -- Tabs: Esc-q toggles tab mode, Esc-i to turns on auto-indent mode

  * Unix emacs -- Tabs: manually set tabs-inserts-spaces mode:<br> <code>M-x set-variable(return) indent-tabs-mode(return) nil</code></li></ul>

<ul><li>Vim, GVim (any OS) -- configure to use Unix line ends and file-type dependent settings: In ~/.vimrc ($HOME/<code>_</code>vimrc on Windows):<br>
<pre><code>set fileformat=unix<br>
filetype plugin indent on<br>
</code></pre>
</li></ul><blockquote>Add $HOME/.vim/ftplugin/python.vim ($HOME/vimfiles/ftplugin/python.vim on Windows) containing:
```
setlocal expandtab shiftwidth=4 shiftround softtabstop=4
```