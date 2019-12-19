### Week 16 Lesson 1 - Intro to D3 Graphing  
* understanding SVG (scalable vector graphics) elements and how to apply/modify using D3
* how to bind data to SVG elements using D3 to create basic bar chart from scratch
* create a bar chart with axes using D3  
[D3 Official Site](https://d3js.org/)  
[D3 Gallery](https://github.com/d3/d3/wiki/Gallery)  
[animated data](https://www.animateddata.com)

01-Evr_Binding_Data  
1) .each() method allows to call function on each element in object. option parameters (d,i).  Similar to using .map() or .forEach() to iterate the array

# ```javascript
>    d3.select("ul").selectAll("li")  
       .each(function(d,i) {  
        console.log("element", this);  
        console.log("data",d);  
        console.log("index",i);  
        }); 
# ```
        
2) .data() allows us to pass array and each item in array to be bound to selected elements one by one.  
3) .text() used with callback function to manipulate elements  
4) .enter() to create sub-selection for data hasn't been mapped.  identifies any DOM elements that need to be added when the joined array is longer than the selection  
5) .append() - Appends a new element with the specified name as the last child of each element in the current selection, returning a new selection containing the appended elements.  
6) .exit() creates selection of surplus and .remove() removes those elements from the DOM

02-Ins_Complex_Data  
* .data() with .enter() creates virtual selection.  .append() appends element to place holder  
* .classed() method allows to asssign class to element. "true" will add class to element while "false" remove class.  

03-Stu_D3_Table  - create D3 table using data binding  
04-Evr_Enter_Exit_Update  
i.  __Basic Data Bind__   
.style() changes the CSS styling of the selected element.    
ii. __Updating New Elements__  
correct class must be given in "ORDER" to apply original styling and adjust height  
iii. __Updating Old elements__  
iv. __Updating Old and New element__  
v. __Exit Patter Revisted__  
vi. __One Function to handle everything__
DRY (do not repeat yourself) - combining into a function will allow to do on the fly.  See activity!

05-Ins_SVG  
* SVG is an XML-based vector image for two-dimensional graphics supports interactivity and animagion.  
[SVG vs PNG](http://www.compatt.com/lab/IandA/IandA_00-00-02.htm)  
tags with svg tell browser which shape is being drawn.  

06-Stu_SVG_Stickman  
[SVG Shape Reference](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Basic_Shapes)  
07-Evr_D3_Bullseye  
[Modifying elements](https://www.d3indepth.com/selections/)  
08-Stu_Data_Rectangles  
09-Stu_UpsideDownBarChart  
10-Evr_Bar_Chart_Refactored  
common practice to use "g" (group) tag for SVG lements.  Allows changes like geometric transformations to be applied to entire group. using attr() to set the transform attribute equal to translate().  
[SVG Coordinates](https://bost.ocks.org/mike/d3/workshop/#106)


### Week 16 Lesson 2 - Bar and Line Charts with D3  
* become more comfortable with data-binding with D3
* import data sets from CSV files (python -m http.server)
* understand how to make a chart responsive on all screen sizes (creating scales and axes in D3)


01-Par_Review_D3
* Review SVG - Scalable Vector Graphics: define own graphics like shapes and lines. IE Custom charts
* Data Binding - binds array of data elements currently on page or to be rendered to page.
* after creating virtual selection use methods .enter() and .append()  


02-Ins_Loading_Data  
* d3.csv() parsing a csv file - similar to d3.json
* explore [Cross Origin Request Errors](https://stackoverflow.com/questions/20041656/xmlhttprequest-cannot-load-file-cross-origin-requests-are-only-supported-for-ht)  
* verse using flask spin up python -m http.server from location of html file trying to render
* using the "+" unary operator casts data as number and shortcut for using parseInt() [unary operators](https://scotch.io/tutorials/javascript-unary-operators-simple-and-useful).  unary operatir is one that takes a single operand/argument and performs an operation.  

03-Par_BarChart_From_CSV  **basic homework initial steps**
* cover g element. Allows for future elements in "group" to be moved relative to SVG
* manipulate chart dimension width and height.  
* create variables that calulate how wide each bar should be to fill whole width of chart and accounts for desired 
    spacing between bars

04-Evr_Scales  

    1) extent() method returns array of minimum and maximum values  
    2) linearScale - ( y = mx + b ) linear equation to interpolate values between domain and range (think continous)  
* D3 scales provide easy way of mapping data values to new values for visualization purposes.
* **domain** is the bounds of the data. example given 
* **range** is the bounds of the chart (corresponds to boundaries of SVG element) and is the set of resulting values 
    of a function.  Range allows data point to be transformed to a corresponding coordinate in the element.
* combine extent() method with scaleLinear in .domain to dynamically pass min and max of array into domain.  Using this
    for both x and y axes would be similar to using autoscale.
3) scaleBand() method used to map categorical data to numerical scale.  Used in bar charts to equally space entire range of chart (think discrete)  
[D3 in Depth](https://www.d3indepth.com/scales/)  
[Scales Tutorial](https://alignedleft.com/tutorials/d3/scales)  **helpful**

05-Ins_Intro_To_Axes  **basic axes manipulation homework**  
    
    1) primary points to remember for data arrays variables - svgHeight, svgWidth, margin, chartHeight, chartWidth, and creation of SVG and g elements  
* .padding() set both inner and outer padding.   
    2) along with axes review how ticks align to outside of chart area when properly placed.  
[Call Method - With call(), an object can use a method belonging to another object.](https://www.w3schools.com/js/js_function_call.asp)  
[D3 Axes](https://github.com/pshrmn/notes/blob/master/d3/axes.md)  

06-Stu_Complete_Bar_Chart  
* practice creating bar chart from CSV data complete with axes.
* ticks() method in y-axis easy way of customizing number of ticks on axis

07-Ins_Line_Generators_Intro  

    1) Part 1: Path HTML  
        * path elemnet and d attribute. d attribute list drawing commands.  path element should also have a stroke, stroke-width, and fill style attributes.  
    2) Part 2: Generating with D3 and Array of points  
        * d3.line() create function able to be passed array of coordinates and create drawing commands for d attribute  
    3) Part 3: Scaling and using accessor functions  
        * data not given as array of coordinates and not appear to be scaled.  
        * .x and .y accessor functions used define how function produce path data. 

08-Stu_Generating_Lines  
* practice using life expectancy data from CSV to generate a line.  
* create a line generator function and store as a variable  

09-Ins_LineChart  
* D3.timeParse() - parsing values as dates  
        a) setting height and width for SVG container  
        b) setting height and width for chart area  
        c) appending svg container to body with dimensions defined earlier  
        d) append SVG group to SVG container within the dimensions of chart area  
[D3.timeParse](https://github.com/d3/d3-time-format)  
[Moment.js](http://momentjs.com/)

10-Stu_LineChart  
same as instructor line chart but with different data and different token for d3.parseTime()  
[locale.format](https://github.com/d3/d3-time-format/blob/master/README.md#locale_format)


### Week 16 Lesson 3 - Line Charts, Scatterplots, and More with D3
* create multiple axes and multiple charts with D3
* be able to create D3 transitions, tooltips, and event listeners
* better understanding of reusable code and javascript functions


01-Evr_Multiline  
* comparing two data sets.  Most same as previous days code with exception of finding max y value to define y axis.  Since two lines will need this to find correct scale  
[D3 Documentation-Time Format ](https://github.com/d3/d3-time-format#locale_format)  
[MDN Web Docs - Conditional Ternary Operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator)  

02-Evr_Multiple_Axes **homework basic multiple axes**  
* two scaling functions for the dependent variable
* create second y-axis on right side of screen
* use appropriate scaling functions in creation of line generators
* for right axis use attr("transform",`translate(${width},0)`.call(rightAxis); correctly place  

[Do's and Don'ts of Dual Axis Charts](https://datahero.com/blog/2015/04/23/the-dos-and-donts-of-dual-axis-charts/)  

03-Evr_Readability  
* add stroke attribute to the g tags containing axes  
* add color coded axes titles by appending "text" elements to the chartGroup  
* text-anchor attribute used to center text around a given point width/2  

04-Stu_Multi_Lines_Axes  
* use CSS styling for x-axis titles  
[MDN - Text Anchor](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/text-anchor)  

05-Evr_Event_Listeners **homework event listener and click events**  
* use event listener .on() function for mouseover and mouseout effect  
* dynamically resize graph as browswer window size changes  
> if (!svgArea.empty()) {
    svgArea.remove();
  }  
* event listner on browser for window resize d3.select(window).on("resize", makeResponsive);    
* for svg container svgHeight and svgWidth set by inner height and width of browser window.innerHeight and window.innerWidth  

06-Ins_Tooltips **homework advanced tooltips basic** 
* circles created at each data point using data binding  
* CSS holds styling for tooltips when rendered!
* .html() tags used to style text or create line breaks (for tooltip)  
[Absolute-Position Tooltip](https://bl.ocks.org/mbostock/1087001)  
[pageX and pageY event](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/pageX)  

07-Stu_Add_Tooltips **homework practice tooltip basic**  
[d3-tip documentation](https://github.com/Caged/d3-tip)  

08-Ins_D3_Tip **homework tooltips using D3-Tip library**  
* using d3-tip library several advantages over previous method  
* using callback function to define HTML features for tooltip 

[d3-Tip more info](http://bl.ocks.org/davegotz/bd54b56723c154d25eedde6504d30ad7)

09-Stu_Hair_Metal **homework scatter plot**  

10-Ins_Transitions  
* Transition is the process of changing from one state to another of an item.  
[D3 transition](https://www.tutorialspoint.com/d3js/d3js_transition.htm)  
[D3 transition basics](https://www.dashingd3js.com/lessons/d3-transition-basics)  

11-Stu_Transitions **homework optional section** 
* will be used to create movement / transition of scatter plot, axis, and labels when changing dimensions  
[D3 transition example](https://bl.ocks.org/d3noob/899a0b2490318a96f9ebd40a5a84e4a7)  

12-Par_Hair_Metal_Conclusion **homework optional section but this is good example**  
* good chance to review code and learn what it is doing.  Functions is JS are important!


# D3 Homework - Data Journalism and D3

![Newsroom](https://media.giphy.com/media/v2xIous7mnEYg/giphy.gif)

## Background

Welcome to the newsroom! You've just accepted a data visualization position for a major metro paper. You're tasked with analyzing the current trends shaping people's lives, as well as creating charts, graphs, and interactive elements to help readers understand your findings.

The editor wants to run a series of feature stories about the health risks facing particular demographics. She's counting on you to sniff out the first story idea by sifting through information from the U.S. Census Bureau and the Behavioral Risk Factor Surveillance System.

The data set included with the assignment is based on 2014 ACS 1-year estimates: [https://factfinder.census.gov/faces/nav/jsf/pages/searchresults.xhtml](https://factfinder.census.gov/faces/nav/jsf/pages/searchresults.xhtml), but you are free to investigate a different data set. The current data set incldes data on rates of income, obesity, poverty, etc. by state. MOE stands for "margin of error."

### Before You Begin

1. Create a new repository for this project called `D3-challenge`. **Do not add this homework to an existing repository**.

2. Clone the new repository to your computer.

3. Inside your local git repository, create a directory for the D3 challenge. Use the folder name to correspond to the challenge: **D3_data_journalism**.

4. This homeworks utilizes both **html** and **Javascript** so be sure to add all the necessary files. These will be the main files to run for analysis.

5. Push the above changes to GitHub or GitLab.

## Your Task

### Level 1: D3 Dabbler

![4-scatter](Images/4-scatter.jpg)

You need to create a scatter plot between two of the data variables such as `Healthcare vs. Poverty` or `Smokers vs. Age`.

Using the D3 techniques we taught you in class, create a scatter plot that represents each state with circle elements. You'll code this graphic in the `app.js` file of your homework directory—make sure you pull in the data from `data.csv` by using the `d3.csv` function. Your scatter plot should ultimately appear like the image at the top of this section.

* Include state abbreviations in the circles.

* Create and situate your axes and labels to the left and bottom of the chart.

* Note: You'll need to use `python -m http.server` to run the visualization. This will host the page at `localhost:8000` in your web browser.

- - -

### Level 2: Impress the Boss (Optional Challenge Assignment)

Why make a static graphic when D3 lets you interact with your data?

![7-animated-scatter](Images/7-animated-scatter.gif)

#### 1. More Data, More Dynamics

You're going to include more demographics and more risk factors. Place additional labels in your scatter plot and give them click events so that your users can decide which data to display. Animate the transitions for your circles' locations as well as the range of your axes. Do this for two risk factors for each axis. Or, for an extreme challenge, create three for each axis.

* Hint: Try binding all of the CSV data to your circles. This will let you easily determine their x or y values when you click the labels.

#### 2. Incorporate d3-tip

While the ticks on the axes allow us to infer approximate values for each circle, it's impossible to determine the true value without adding another layer of data. Enter tooltips: developers can implement these in their D3 graphics to reveal a specific element's data when the user hovers their cursor over the element. Add tooltips to your circles and display each tooltip with the data that the user has selected. Use the `d3-tip.js` plugin developed by [Justin Palmer](https://github.com/Caged)—we've already included this plugin in your assignment directory.

![8-tooltip](Images/8-tooltip.gif)

* Check out [David Gotz's example](https://bl.ocks.org/davegotz/bd54b56723c154d25eedde6504d30ad7) to see how you should implement tooltips with d3-tip.

- - -

### Assessment

Your final product will be assessed on the following metrics:

* Creation of a **new** repository on GitHub called `D3-Challenge` (note the kebab-case). Do not add to an already existing repo.

* Completion of all steps in chosen level

* Coherency of scatter plot (labels, ticks)

* Visual attraction

* Professionalism

**Good luck!**

### Copyright

Trilogy Education Services © 2019. All Rights Reserved.