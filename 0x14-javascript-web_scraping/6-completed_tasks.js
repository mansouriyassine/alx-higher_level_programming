#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('error:', error);
    return;
  }

  const todos = JSON.parse(body);
  const completedTasks = {};

  todos.forEach(task => {
    if (task.completed) {
      if (completedTasks[task.userId] === undefined) {
        completedTasks[task.userId] = 0;
      }
      completedTasks[task.userId]++;
    }
  });

  console.log(completedTasks);
});
