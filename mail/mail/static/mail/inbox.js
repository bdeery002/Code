document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);


  // Handle compose form submission
  document.querySelector('#compose-form').addEventListener('submit', function(event) {
    console.log('form submitted');  // ADD THIS
    event.preventDefault();

    fetch('/emails', {
      method: 'POST',
      body: JSON.stringify({
        recipients: document.querySelector('#compose-recipients').value,
        subject:    document.querySelector('#compose-subject').value,
        body:       document.querySelector('#compose-body').value
      })
    })
    .then(response => response.json())
    .then(result => {
      if (result.error) {
        alert(result.error);
      } else {
        load_mailbox('sent');
      }
    });
  });

  // By default, load the inbox
  load_mailbox('inbox');
});


function compose_email() {
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // Fetch emails for this mailbox
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {

    if (emails.error) {
      console.log(emails.error);
      return;
    }

    // Render each email as a row
    emails.forEach(email => {
      const row = document.createElement('div');

      row.innerHTML = `
        <span><strong>${email.sender}</strong></span>
        <span>${email.subject}</span>
        <span style="float:right">${email.timestamp}</span>
      `;

      // White if unread, gray if read
      row.style.backgroundColor = email.read ? '#d3d3d3' : 'white';
      row.style.border = '1px solid #ccc';
      row.style.padding = '8px';
      row.style.marginBottom = '4px';
      row.style.cursor = 'pointer';

      document.querySelector('#emails-view').append(row);
    });
  });
}