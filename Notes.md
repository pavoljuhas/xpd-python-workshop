# Mercurial HOWTOs #

To obtain updates from the MAIN repository do:
```
hg commit
hg pull -r BMAIN MAIN
hg update
# if there is a message about "across branches update" do:
hg merge BMAIN
hg commit
```

To send your local revisions to your personal project clone at Google Code:
```
hg push -r .
```