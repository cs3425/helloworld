

# helloworld

### Installation 
Clone the repo and use pip to install it. 
```bash
git clone https://github.com/cs3425/helloworld.git
cd helloworld/
pip install .
```

### CLI Usage 
To use the executable helloworld command line program:
```
$ helloworld -h
usage: helloworld [-h] [--name] [--aday] [--temp]

arguments:
  -h, --help            show this help message and exit
  --name                optional name to say hello to
  --aday                print a date to plan a hairstyle for you
  --temp                print the temperature to pick a food for you
```


### API Usage
To use the helloworld Python API:
```python
import helloworld
helloworld.helloworld(name="Cecilia", aday=1, temp=66)
```

```
hello Cecilia
Wear princess leia buns on that day!
You should eat enchiladas
```
