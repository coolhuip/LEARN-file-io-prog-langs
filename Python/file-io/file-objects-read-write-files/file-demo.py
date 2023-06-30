"""
Python Tutorial: File Objects - Reading and Writing to Files
https://www.youtube.com/watch?v=Uh2ebFW8OYM&ab_channel=CoreySchafer


NOTE:
my_file = open( 'directory/file.extension' , 'r|w|a|r+|w+|a+' )

NOTE:
r = read
w = write
a = append
r+ = read + write
w+ = read + write (truncate)
a+ = read + append

NOTE:
my_file.seek( n )  =>  Move the cursor to the n-th char position
                       in the file (starts from 0).

my_file.tell() => Return the current char position.

NOTE:
When read(), readlines(), or readline() reaches EOF,
it returns an empty string.
"""

from __future__ import annotations


print("=====================================================================")
print()


# This is NOT a good way to handle files.
f1 = open('test.txt', 'r')
print(f1.name)
print(f1.mode)
f1.mode = 'w'
print("file access mode has been changed to:")
print(f1.mode)
f1.close()


# Instead, use a CONTEXT MANAGER.
print()
with open('test.txt', 'r') as f2:
    print(f2.name)
    print(f2.mode)
    f2.mode = 'w'
    print("file access mode has been changed to:")
    print(f2.mode)
    print(f2.closed)

print(f2.closed)


# Read line-by-line METHOD #1
print()
with open('test.txt', 'r') as f3:
    print(f3.readline(), end='')
    print(f3.readline(), end='')
    print(f3.readline(), end='')


# Read line-by-line METHOD #2
print()
with open('test.txt', 'r') as f4:
    # readlines() => list[str]
    for line in f4.readlines():
        print(line, end='')


# Read line-by-line METHOD #3
print()
with open('test.txt', 'r') as f5:
    for line in f5:
        print(line, end='')


# Read by char count
print()
with open('test.txt', 'r') as f6:
    f6_contents = f6.read(16)
    print(f6_contents, end='')
    print('___________')
    f6_contents = f6.read(153)
    print(f6_contents, end='')
    print('___________')
    f6_contents = f6.read(1000)  # EOF reached way before 1000 characters
    print(f6_contents, end='')


# Read by char count (MORE CONTROL)
print()
with open('test.txt', 'r') as f7:
    size_to_read = 3

    f7_contents = f7.read(size_to_read)
    while len(f7_contents):
        print(f7_contents, end='_')
        f7_contents = f7.read(size_to_read)
    

# Adjust the file pointer/cursor via seek()
print()
with open('test.txt', 'r') as f8:
    size_to_read = 20
    print(f8.read(size_to_read), end='')
    # Now, go back to char position 0 and read 19 characters.
    f8.seek(0)
    print(f8.read(size_to_read), end='')
    # Now, go back to char position 1 and read 19 characters.
    f8.seek(1)
    print(f8.read(size_to_read))


# The 'w' modifier (if file already exists) will wipe out the existing content
# and overwrite from char-pos 0.
#     -> To prevent this, use the 'a' modifier, instead.
print()
with open('test2.txt', 'w') as f9:
    f9.write('Test')
    f9.write('Test_')
    f9.seek(0)
    f9.write('777')
    f9.seek(10)
    f9.write('\n  bruh')


# Read + Write on multiple files at the same time (i.e., copy files).
with open('test.txt', 'r') as rf:
    with open('test3.txt', 'w') as wf:
        for line in rf.readlines():
            wf.write(line)
        # OR, we can read line-by-line without calling rf.readlines()
        rf.seek(1), wf.seek(10)
        for line in rf:
            wf.write(line)


# Finally, let's copy a large .JPG image instead of a text file.
with open('rasta-banana.jpg', 'rb') as rf:
    with open('rasta-banana_COPY.jpg', 'wb') as wf:
        chunk_size = 9000
        rf_chunk = rf.read(chunk_size)
        wf.write(rf_chunk)


# Oops! We only copied the first 9 kilobytes of our original img there...
# Now, let's do it right & copy the whole thing.
with open('rasta-banana.jpg', 'rb') as rf:
    with open('rasta-banana_COPY_2.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk):
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)


print("=====================================================================")
