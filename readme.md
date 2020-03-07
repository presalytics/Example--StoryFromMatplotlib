# Example--StoryFromMatplotlib

This simple example walks through how to create story from a matplotlib chart and share it through the Presaltyics API.  This example is meant to help new users understand how presalytics works and demonstrate basic features.

### Getting Started

You can get started by cloning this repository from the command line:
~~~~bash
git clone https://github.com/presalytics/Example--InteroperableStory.git
~~~~

Then create a python virtual environment and install the required packages via pip:
~~~~bash
python3 -m venv venv
. venv/bin/activate # venv\Scripts\activate.bat on Windows
pip install presalytics sklearn
~~~~

To use this environment as a presalytics workspace, it needs a `config.py` file.  Generate a config.py
file with the following command:

~~~~bash
presalytics config {YOUR_USERNAME}
~~~~

where `{YOUR_USERNAME}` is the username that you use to login to [Presaltyics.io](https://presalytics.io).  If you dont yet have an account, you can [sign up here](https://presalytics.io/accounts/signup/).

### Understanding example.py

`example.py` is a simple that generates a scatterplot using the matplotlib library.  The scatterplot is a stand-in for analysis that you can do and display in a chart via matplotlib.  

There are two noteworthy lines in this file that are different: the first and last lines of the script.  The first line is stardard import for the Presalytics Python Library.  The last line creates a "widget".   

~~~~python
# example.py

import presalytics # <-- presalytics library import
import matplotlib.pyplot as plt
import numpy as np
 
x = np.random.rand(30)
y = np.random.rand(30)
z = np.random.rand(30)
 
fig, ax = plt.subplots()

ax.scatter(x, y, s=z*1000, alpha=0.5)

example = presalytics.MatplotlibResponsiveFigure(fig, "BubbleChart")  # <-- Creation of widget
~~~~

We'll use the [MatplotlibResponsiveFigure](https://presalytics.github.io/python-client/presalytics/index.html#presalytics.MatplotlibResponsiveFigure) widget on the last line that we named "BubbleChart" in the next step to create and view a story.

### Creating and viewing a story

From the terminal, run the commmand:

~~~~bash
presalytics --manage create BubbleChart --widget
~~~~

After authenticating, this command does a few things:

1. Executes the python module `example.py` and loads the "BubbleChart" widget into the presaltyics widget registry
2. Creates a [Story Outline](https://presalytics.github.io/python-client/presalytics/index.html#presalytics.StoryOutline) and saves it in a file call `story.yaml`
3. Uploads the new Story Outline to the Presaltyics API and creates a Story (https://presaltyics.io/docs/how-it-works/stories/)
4. Open the story management page on [Presalytics.io](https://presalytics.io) in a new browser tag

### The Story Management Page

Now, your default web browser should now be open with a new tab that has loaded the management page for the story.  At the top of the page, you will see few navigation buttons and a render view of the story bubble chart that you ust created:

![Top of Manage Page](https://raw.githubusercontent.com/presalytics/Example--StoryFromMatplotlib/master/manage-top.PNG)

As you scroll down the page, you find a section to view and update story metadata:

![Story Properties](https://raw.githubusercontent.com/presalytics/Example--StoryFromMatplotlib/master/properties.PNG)

Below the the properties, you'll see a section to help you share the story with co-workers and manage the editing rights of the users with access to the story:

![Story Collaborate Image](https://raw.githubusercontent.com/presalytics/Example--StoryFromMatplotlib/master/collaborate.PNG)

In this section, if you click on the "Share With a Colleague" button, a modal window will pop up.  Enter the email address of someone that you want to share the story with, and the Presalytics API will send them an email asking them to view it.

![Share modal Image](https://raw.githubusercontent.com/presalytics/Example--StoryFromMatplotlib/master/share-modal.PNG)


Add the bottom of the page, you'll see a JSON editor with the story outline.  Here, you can make view the story outline, make edits and save changes.  But be careful... ill-advied changes to the outline will cause the story to fail to render.

![Outline Editor](hhttps://raw.githubusercontent.com/presalytics/Example--StoryFromMatplotlib/master/edit-outline.PNG)


# Conclusion

This example walks users through how to set up a presaltyics workspace, build and edit a simple story, and share that story with friends and co-workers.  If you have any questions about this example or would like help with your use case, please shoot us an email at [inquires@presalytics.io](mailto:inquires@presalytics.io).