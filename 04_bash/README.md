# Debugging Bash

Below is the contents of the Bash script `myscript.sh`:

```bash
#!/bin/bash

echo "Number of command line parameters: $#"
echo "All the command line parameters: $@"

UPPER=3
for i in `seq $UPPER`; do
    echo $i
done

if [ $1 -ge 3 ]; then
    echo "$1 > 3"
fi

hostname
```

Execute the script in standard mode:

```bash
$ cd intro_debugging/04_bash
$ bash mybash.sh 42 43 44
Number of command line parameters: 3
All the command line parameters: 42 43 44
1
2
3
42 > 3
mbp2019.local
```

Now use the `-x` option to run the script in pseudo-debugging mode:

```bash
$ bash -x myscript.sh 42 43 44
+ echo 'Number of command line parameters: 3'
Number of command line parameters: 3
+ echo 'All the command line parameters: 42' 43 44
All the command line parameters: 42 43 44
+ UPPER=3
++ seq 3
+ for i in '`seq $UPPER`'
+ echo 1
1
+ for i in '`seq $UPPER`'
+ echo 2
2
+ for i in '`seq $UPPER`'
+ echo 3
3
+ '[' 42 -ge 3 ']'
+ echo '42 > 3'
42 > 3
+ hostname
mbp2019.local
```

See also the [Bash debugger](http://bashdb.sourceforge.net) project.
