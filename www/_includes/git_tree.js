// This file should be generated from the .git
/***********************
 *  CUSTOM TEMPLATES   *
 ***********************/

var myTemplateConfig = {
  colors: ["#F00", "#0F0", "#00F"], // branches colors, 1 per column
  branch: {
    lineWidth: 5,
    spacingX: 40
  },
  commit: {
    spacingY: -40,
    dot: {
      size: 8
    },
    message: {
      displayAuthor: true,
      displayBranch: true,
      displayHash: true,
      font: "normal 12pt Arial"
    },
    tooltipHTMLFormatter: function(commit) {
      return "<b>" + commit.sha1 + "</b>" + ": " + commit.message;
    }
  }
};
var myTemplate = new GitGraph.Template(myTemplateConfig);

/***********************
 *    INITIALIZATION   *
 ***********************/

var config = {
  template: "metro" // could be: "blackarrow" or "metro" or `myTemplate` (custom Template object)
    //, mode: "compact"     // special compact mode : hide messages & compact graph
};
var gitGraph = new GitGraph(config);

/***********************
 * BRANCHS AND COMMITS *
 ***********************/

// Create branch named "master"
var master = gitGraph.branch("master");

// Commit on HEAD Branch which is "master"
gitGraph.commit("Initial commit");

// Add few commits on master.
gitGraph.commit("My second commit").commit("Add awesome feature");

// Create a new "dev" branch from "master"
var dev = gitGraph.branch("dev");
dev.commit("Youhou \\o/");

// Commit again on "master"
master.commit("I'm the master !");

master.merge(dev, "Resolving merge conflicts");
// Advanced commit method with style and specific author (HEAD)
var commitConfig = {
  dotColor: "white",
  dotSize: 10,
  dotStrokeWidth: 10,
  messageHashDisplay: false,
  messageAuthorDisplay: true,
  message: "Alors c'est qui le papa ?",
  author: "Me <me@planee.fr>"
};
gitGraph.commit(commitConfig);

/***********************
 *      CHECKOUT       *
 ***********************/

// Checkout on master branch for create "test" since master
//master.checkout();

/***********************
 *       DETAILS       *
 ***********************/

var commitWithDetailsConfig = {
  message: "test",
  detail: "detail" // Id of detail div (available in normal vertical mode only)
};
gitGraph.commit(commitWithDetailsConfig).commit();
dev.commit().commit(); // 2 default Commit on "dev"

/***********************
 *    CUSTOMIZATION    *
 ***********************/

gitGraph.author = "Fabien0102 <fabien0102@planee.fr>";
master.commit();

/***********************
 *       MERGES        *
 ***********************/

master.checkout();

// Merge "dev" branch into HEAD (which is "master"), with a default message
dev.merge();

// Create a "test" branch and merge in into "master" with a custom message and tag.
var test = gitGraph.branch({
    message: "Branching test",
    onClick: (event) => console.log("You clicked on a branching point", event.data)
});
test.commit("Final commit");
test.merge(master, "My special merge commit message");

// Then, continue committing on the "test" branch
test.commit({
  message: "It works !"
});

/***********************
 *        TAGS         *
 ***********************/

// Add a tag to a commit
test.commit({
  message: "{{site.github.repository_url}}",
  tag: "a-tag",
  onClick: (event) => console.log("You clicked the last commit", event)
});

// Perform a merge, with a tag
test.merge(master, {
  message: "New release",
  tag: "v1.0.0",
  onClick: (event) => console.log("You clicked the release Commit", event)
});


/***********************
 *       EVENTS        *
 ***********************/

gitGraph.canvas.addEventListener("commit:mouseover", function(event) {
  console.log("You're over a commit.", "Here is a bunch of data ->", event);
});
