var express = require("express");
var got = require("got");
var uuid = require("uuid").v4;

var router = express.Router();

var secretKey = "test_ak_ZORzdMaqN3wQd5k6ygr5AkYXQGwy";

router.get("/settlement", function (req, res) {
  let startDate = "2022-03-01";
  let endDate = "2022-03-31";
  let page = 1;
  let size = 100;

  got(
    "https://api.tosspayments.com/v1/settlements" +
      "?startDate=" +
      startDate +
      "&endDate=" +
      endDate +
      "&page=" +
      page +
      "&size=" +
      size,
    {
      headers: {
        Authorization:
          "Basic " + Buffer.from(secretKey + ":").toString("base64"),
      },
      responseType: "json",
    }
  )
    .then(function (response) {
      res.render("settlement", {
        isSuccess: true,
        responseJson: response.body,
      });
    })
    .catch(function (error) {
      res.render("settlement", {
        isSuccess: false,
        rresponseJson: error.response.body,
      });
    });
});

module.exports = router;
