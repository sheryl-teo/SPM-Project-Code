
import React from 'react';
import "./LJ_Creation_Page.css"

const LJCreationPage = () => {
  return (
    <div className='creation'>
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css"
        integrity="sha384-9gVQ4dYFwwWSjIDZnLEWnxCjeSWFphJiwGPXr1jddIhOegiu1FwO5qRGvFXOdJZ4"
        crossorigin="anonymous"></link>
      <form action="" method='post'>
        <h1>Registration Form</h1>
        <p>
          <input type="text" name="name" class="formStyle" placeholder="Name (required)" required />
        </p>
        <p>
          <input type="text" name="id" class="formStyle" placeholder="Staff_ID (required)" required />
        </p>
        <p>
          <select class="selectpicker" data-size="4">
            <option value="">Select Custom Field</option>
            <option value="nickname">nickname</option>
            <option value="first_name">first_name</option>
          </select>
        </p>
        <a href="#" class="formButton">Subscribe</a>
      </form>
    </div>
  );
};

export default LJCreationPage;