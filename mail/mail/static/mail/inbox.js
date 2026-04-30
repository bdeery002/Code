
// Wait for the entire HTML page to finish loading before running any JS
document.addEventListener('DOMContentLoaded', function() {

  //// Attach click listeners to the nav buttons in inbox.html. those are the 4 buttons in under the first h2 in inbox.html.
  //  when the user clicks on one of those buttons, the corresponding function will be called. 
  // for example, if the user clicks on the "Inbox" button, the load_mailbox function will be called with the argument 'inbox'. this will load the inbox view and display all emails in the inbox.
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // Handle compose form submission
  document.querySelector('#compose-form').addEventListener('submit', function(event) {
    // Prevent the browser's default behaviour of reloading the page on form submit
    event.preventDefault();

    // fetch() sends an HTTP request to your Django backend.
    // Here we're sending a POST request to the /emails route.
    fetch('/emails', {
      method: 'POST',

        // JSON.stringify converts the JS object into a JSON string so it can be sent over HTTP.
        // We're pulling the values the user typed into the compose form fields.

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
  document.querySelector('#email-view').style.display = 'none';

  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}


function load_mailbox(mailbox) {
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#email-view').style.display = 'none';

  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {

    if (emails.error) {
      console.log(emails.error);
      return;
    }

    emails.forEach(email => {
      const row = document.createElement('div');

      row.innerHTML = `
        <span><strong>${email.sender}</strong></span>
        <span>${email.subject}</span>
        <span style="float:right">${email.timestamp}</span>
      `;

      row.style.backgroundColor = email.read ? '#d3d3d3' : 'white';
      row.style.border = '1px solid #ccc';
      row.style.padding = '8px';
      row.style.marginBottom = '4px';
      row.style.cursor = 'pointer';

      row.addEventListener('click', () => view_email(email.id));
      document.querySelector('#emails-view').append(row);
    });
  });
}


function view_email(id) {
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#email-view').style.display = 'block';

  fetch(`/emails/${id}`)
  .then(response => response.json())
  .then(email => {

    document.querySelector('#email-view').innerHTML = `
      <div><strong>From:</strong> ${email.sender}</div>
      <div><strong>To:</strong> ${email.recipients.join(', ')}</div>
      <div><strong>Subject:</strong> ${email.subject}</div>
      <div><strong>Timestamp:</strong> ${email.timestamp}</div>
      <hr>
      <div>${email.body}</div>
    `;

    const archiveBtn = document.createElement('button');
    archiveBtn.textContent = email.archived ? 'Unarchive' : 'Archive';
    archiveBtn.className = 'btn btn-sm btn-outline-primary';

    archiveBtn.addEventListener('click', () => {
      fetch(`/emails/${id}`, {
        method: 'PUT',
        body: JSON.stringify({ archived: !email.archived })
      })
      .then(() => load_mailbox('inbox'));
    });

   document.querySelector('#email-view').append(archiveBtn);

    // Reply button
    const replyBtn = document.createElement('button');
    replyBtn.textContent = 'Reply';
    replyBtn.className = 'btn btn-sm btn-outline-primary';
    replyBtn.style.marginLeft = '5px';

    replyBtn.addEventListener('click', () => {
      compose_email();
      document.querySelector('#compose-recipients').value = email.sender;
      document.querySelector('#compose-subject').value = email.subject.startsWith('Re: ')
        ? email.subject
        : `Re: ${email.subject}`;
      document.querySelector('#compose-body').value = `On ${email.timestamp} ${email.sender} wrote:\n${email.body}`;
    });

    document.querySelector('#email-view').append(replyBtn);

    // Mark as read
    fetch(`/emails/${id}`, {
      method: 'PUT',
      body: JSON.stringify({ read: true })
    });


  });
}