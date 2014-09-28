"use strict";

var path = require("path");

module.exports = {
    root: path.resolve("./"), // Path to css, js and img folders
    excludedJsFolder: "libs", // Folder to exclude for jshint
    beep: true, // Beep on error
    cssRules: {
        strictPropertyOrder: true, // Complains if not strict property order
        noIDs: true, // Complains about using IDs in your stylesheet
        noJSPrefix: true, // Cmplains about styling .js- prefixed classnames
        noOverqualifying: true, // Complains about overqualified selectors
        noUnderscores: true, // Complains about using underscores in your class names
        noUniversalSelectors: true, // Complains about using the universal * selector
        zeroUnits: true // Complains if you add units to values of 0
    }
};
