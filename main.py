# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Read CSV file

import csv

with open('slodkie.csv', newline='') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')

    html_code = ""

    for row in csvreader:
        # For every row in css create div
        divstr = f"""
           <div class="border">
                <div class="grid-container">
                  <div class="item1">
                    <div class="season">
                        <div class="circle spring"></div>
                        <div class="circle summer"></div>
                        <div class="circle autumn"></div>
                        <div class="circle winter"></div>
                    </div>
                  </div>
                  <div class="item2">
                    <div class="person">
                        <i class="text-grey">M</i>
                        <i class="text-grey">B</i>
                        <i class="text-grey">F</i>
                        <i class="text-grey">M</i>
                    </div>
                  </div>
                  <div class="item3">
                    <div class="main">
                        {row['Name']}
                    </div>
                  </div>
                  <div class="item4">
                    <div class="source">
                        {row['Source']}
                    </div>
                  </div>
                  <div class="item5">
                    <div class="veggies">
                        <div class="carrot">
                            <i class="fas fa-carrot"> </i>
                        </div>
                    </div>
                  </div>
                </div>
            </div>
        """

        # concatenate with other divs
        html_code = html_code + divstr


# replace 'placeholder' in html and save as new HTML
with open('food-card-template.html', 'r') as file :
    filedata = file.read()

# Replace the target string
filedata = filedata.replace('placeholder', html_code)

# Write the file out again
with open('food-card-slodkie.html', 'w') as file:
    file.truncate(0)
    file.write(filedata)


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':



# See PyCharm help at https://www.jetbrains.com/help/pycharm/


