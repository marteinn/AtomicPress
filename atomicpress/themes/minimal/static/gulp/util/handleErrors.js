"use strict";

var gutil = require("gulp-util"),
    config = require("../config");

// Handle an error based on its severity level.
// Log all levels, and exit the process for fatal levels.
function handleError(stop, error) {
    gutil.log(error.message);

    if (config.beep) {
        gutil.beep();
    }

    if (stop) {
        process.exit(1);
    }
}

// Convenience handler for error-level errors.
exports.error = function(error) {
    handleError.call(this, true, error);
};
// Convenience handler for warning-level errors.
exports.warning = function(error) {
    handleError.call(this, false, error);
};
