import time
import makeArray

# sorting algorithms
from quickSort import quickSort, modified_quickSort
from timSort import TimSort
from radix import radixsort

from rbtrees import RedBlackTree

def testQuickSort(trial_amount):
    trial_times_for_unique = []
    trial_times_for_1p = []
    trial_times_for_20size = []

    print("\n\nStarting unique array trials")
    for index in range(1, ( trial_amount + 1) ):
        print("Starting trial: U{}".format(index))

        # generate unique array
        unique_array = makeArray.generateUniqueArray();

        # starting trial time
        start = time.time()

        # run trial
        quickSort(unique_array)

        # gets trial end time
        end = time.time()

        # outputs trial time
        print("elapsed time: ", (end - start) )
        trial_times_for_unique.append( {
            'trial':index,
            'time':(end - start)
        } )

    print("\n\nStarting 1% array trials")
    for index in range(1, ( trial_amount + 1) ):
        print("Starting trial: p{}".format(index))

        # generate unique array
        unique_array = makeArray.generate1pArray();

        # starting trial time
        start = time.time()

        # run trial
        quickSort(unique_array)

        # gets trial end time
        end = time.time()

        # outputs trial time
        print("elapsed time: ", (end - start) )
        trial_times_for_1p.append( {
            'trial':index,
            'time':(end - start)
        } )

    print("\n\nStarting 20sized array trials")
    for index in range(1, ( trial_amount + 1) ):
        print("Starting trial: s{}".format(index))

        # generate unique array
        unique_array = makeArray.generate20intArray();

        # starting trial time
        start = time.time()

        # run trial
        quickSort(unique_array)

        # gets trial end time
        end = time.time()

        # outputs trial time
        print("elapsed time: ", (end - start) )
        trial_times_for_20size.append( {
            'trial':index,
            'time':(end - start)
        } )

    all_trials = {
        'quickSort_unique':trial_times_for_unique,
        'quickSort_1p':trial_times_for_1p,
        'quickSort_20size':trial_times_for_20size
    }

    print("")
    for key in all_trials:
        print(key,": ")
        for trial in all_trials[key]:
            print(trial)
        print("")

    return all_trials

def testModifiedQuickSort(trial_amount):
    trial_times_for_unique = []
    trial_times_for_1p = []
    trial_times_for_20size = []

    print("\n\nStarting unique array trials")
    for index in range(1, ( trial_amount + 1) ):
        print("Starting trial: U{}".format(index))

        # generate unique array
        unique_array = makeArray.generateUniqueArray();

        # starting trial time
        start = time.time()

        # run trial
        modified_quickSort(unique_array)

        # gets trial end time
        end = time.time()

        # outputs trial time
        print("elapsed time: ", (end - start) )
        trial_times_for_unique.append( {
            'trial':index,
            'time':(end - start)
        } )

    print("\n\nStarting 1% array trials")
    for index in range(1, ( trial_amount + 1) ):
        print("Starting trial: p{}".format(index))

        # generate unique array
        unique_array = makeArray.generate1pArray();

        # starting trial time
        start = time.time()

        # run trial
        modified_quickSort(unique_array)

        # gets trial end time
        end = time.time()

        # outputs trial time
        print("elapsed time: ", (end - start) )
        trial_times_for_1p.append( {
            'trial':index,
            'time':(end - start)
        } )

    print("\n\nStarting 20sized array trials")
    for index in range(1, ( trial_amount + 1) ):
        print("Starting trial: s{}".format(index))

        # generate unique array
        unique_array = makeArray.generate20intArray();

        # starting trial time
        start = time.time()

        # run trial
        modified_quickSort(unique_array)

        # gets trial end time
        end = time.time()

        # outputs trial time
        print("elapsed time: ", (end - start) )
        trial_times_for_20size.append( {
            'trial':index,
            'time':(end - start)
        } )

    all_trials = {
        'modifiedquickSort_unique':trial_times_for_unique,
        'modifiedquickSort_1p':trial_times_for_1p,
        'modifiedquickSort_20size':trial_times_for_20size
    }

    print("")
    for key in all_trials:
        print(key,": ")
        for trial in all_trials[key]:
            print(trial)
        print("")

    return all_trials

def testRadixSort(trial_amount):
    trial_times_for_unique = []
    trial_times_for_1p = []
    trial_times_for_20size = []

    print("\n\nStarting unique array trials")
    for index in range(1, ( trial_amount + 1) ):
        print("Starting trial: U{}".format(index))

        # generate unique array
        unique_array = makeArray.generateUniqueArray();

        # starting trial time
        start = time.time()

        # run trial
        radixsort(unique_array)

        # gets trial end time
        end = time.time()

        # outputs trial time
        print("elapsed time: ", (end - start) )
        trial_times_for_unique.append( {
            'trial':index,
            'time':(end - start)
        } )

    print("\n\nStarting 1% array trials")
    for index in range(1, ( trial_amount + 1) ):
        print("Starting trial: p{}".format(index))

        # generate unique array
        unique_array = makeArray.generate1pArray();

        # starting trial time
        start = time.time()

        # run trial
        radixsort(unique_array)

        # gets trial end time
        end = time.time()

        # outputs trial time
        print("elapsed time: ", (end - start) )
        trial_times_for_1p.append( {
            'trial':index,
            'time':(end - start)
        } )

    print("\n\nStarting 20sized array trials")
    for index in range(1, ( trial_amount + 1) ):
        print("Starting trial: s{}".format(index))

        # generate unique array
        unique_array = makeArray.generate20intArray();

        # starting trial time
        start = time.time()

        # run trial
        radixsort(unique_array)

        # gets trial end time
        end = time.time()

        # outputs trial time
        print("elapsed time: ", (end - start) )
        trial_times_for_20size.append( {
            'trial':index,
            'time':(end - start)
        } )

    all_trials = {
        'radixSort_unique':trial_times_for_unique,
        'radixSort_1p':trial_times_for_1p,
        'radixSort_20size':trial_times_for_20size
    }

    print("")
    for key in all_trials:
        print(key,": ")
        for trial in all_trials[key]:
            print(trial)
        print("")

    return all_trials

def testTimSort(trial_amount):
    trial_times_for_unique = []
    trial_times_for_1p = []
    trial_times_for_20size = []

    print("\n\nStarting unique array trials")
    for index in range(1, ( trial_amount + 1) ):
        print("Starting trial: U{}".format(index))

        # generate unique array
        unique_array = makeArray.generateUniqueArray();

        # starting trial time
        start = time.time()

        # run trial
        TimSort(unique_array)

        # gets trial end time
        end = time.time()

        # outputs trial time
        print("elapsed time: ", (end - start) )
        trial_times_for_unique.append( {
            'trial':index,
            'time':(end - start)
        } )

    print("\n\nStarting 1% array trials")
    for index in range(1, ( trial_amount + 1) ):
        print("Starting trial: p{}".format(index))

        # generate unique array
        unique_array = makeArray.generate1pArray();

        # starting trial time
        start = time.time()

        # run trial
        TimSort(unique_array)

        # gets trial end time
        end = time.time()

        # outputs trial time
        print("elapsed time: ", (end - start) )
        trial_times_for_1p.append( {
            'trial':index,
            'time':(end - start)
        } )

    print("\n\nStarting 20sized array trials")
    for index in range(1, ( trial_amount + 1) ):
        print("Starting trial: s{}".format(index))

        # generate unique array
        unique_array = makeArray.generate20intArray();

        # starting trial time
        start = time.time()

        # run trial
        TimSort(unique_array)

        # gets trial end time
        end = time.time()

        # outputs trial time
        print("elapsed time: ", (end - start) )
        trial_times_for_20size.append( {
            'trial':index,
            'time':(end - start)
        } )

    all_trials = {
        'timSort_unique':trial_times_for_unique,
        'timSort_1p':trial_times_for_1p,
        'timSort_20size':trial_times_for_20size
    }

    print("")
    for key in all_trials:
        print(key,": ")
        for trial in all_trials[key]:
            print(trial)
        print("")

    return all_trials

def formatCSVForNTrials(csv_name, n):
    with open(csv_name,'w') as csv:
        write_string = "Trials:,"
        for index in range(1, (n + 1) ):
            write_string += str(index) + ','
        write_string += ',average,\n\n'
        csv.write(write_string);
    return

def writeDataToCSV(csv_name, data_to_write):
    global NumberOfTrials
    with open(csv_name,'a') as csv:
        for key in data_to_write:
            write_string = str(key) + ":,"
            running_time = 0
            for trial in data_to_write[key]:
                write_string += str(trial['time']) + ','
                running_time += trial['time']

            write_string += ',' + str( running_time/NumberOfTrials ) + ',\n'
            csv.write(write_string)

        csv.write('\n\n')

NumberOfTrials = 50;
csv_name = 'data2.csv'
formatCSVForNTrials(csv_name,NumberOfTrials);
quickSort_trials = testQuickSort(NumberOfTrials);
writeDataToCSV(csv_name, quickSort_trials)
modifiedquickSort_trials = testModifiedQuickSort(NumberOfTrials);
writeDataToCSV(csv_name, modifiedquickSort_trials)
radixSort_trials = testRadixSort(NumberOfTrials);
writeDataToCSV(csv_name, radixSort_trials)
timSort_trials = testTimSort(NumberOfTrials);
writeDataToCSV(csv_name, timSort_trials)
