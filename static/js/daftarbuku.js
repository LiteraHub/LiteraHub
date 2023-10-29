let card = document.querySelectorAll('.card.scale-up');
let closeightside = document.querySelector('.closerightside');
let rightside = document.querySelector('.right-side');
let parentcard = document.querySelector('.row.parentcard');
let container = document.querySelector('.container.mt-4');

//Menghandle Scroll kebawah
window.onscroll = function() {
  if (document.body.scrollTop > 160 || document.documentElement.scrollTop > 160) {
    document.querySelector(".right-side").style.position = "fixed";
    document.querySelector(".right-side").style.top = "0";
    document.querySelector(".right-side").style.marginTop = "0";
  }
  else {
    // Kembalikan properti ke nilai aslinya ketika scroll kurang dari 50
    document.querySelector(".right-side").style.position = "absolute";
    document.querySelector(".right-side").style.removeProperty("top") // Atur kembali ke nilai awal
    document.querySelector(".right-side").style.marginTop = "1.5rem"; // Atur kembali ke nilai awal
  }
};

// Menambahkan event listener ke setiap elemen card
card.forEach(card => {
  card.addEventListener('click', () => {
    rightside.classList.add('active');
    parentcard.classList.add('active');
    container.classList.add('active');
    let id = card.querySelector('#pkbuku').textContent;
    // console.log(id);
    let title = card.querySelector('#title').textContent;
    $.ajax({
        method: 'GET',
        url: '/daftarbuku/choose-book/',
        headers: {
            'X-CSRFToken': getCsrfToken(),
        },
        data: {title: title, id:id},
        success: function(data) {
            refreshCard(data);
            refreshReview(data);
        },
        error: function(error) {
            alert('Error on fetching articles from server.')
        },
    });
    document.getElementById("button_addreview").onclick = function(){
      addReview(id);
    };
  })
});

async function refreshReview(data){
  if (data.length>1){
    let reviewbook = $('#reviewbook');
    reviewbook.empty();
    for (let i = 1; i < data.length+1; i++) {
      let name = data[i].user.name;
      console.log(name);
      let review = data[i].review;
      let created_at = data[i].created_at;
      reviewbook.append(`
        <div style="background-color: #f2eee3; margin-left: 1rem; margin-right: 2rem; max-height: 17rem; overflow: auto;">
          <h6>@${name}<span style="margin-left: 1rem">${created_at}</span></h6>
          <div style="background-color: #f2eee3; margin-left: 1.5rem;">
            <p>${review}</p>
          </div>
        </div>
      `);
    }
  }
  else{
    let reviewbook = $('#reviewbook');
    reviewbook.empty();
    reviewbook.append(`
        <div style="background-color: #f2eee3; margin-left: 2rem; margin-right: 2rem; height: 17rem; overflow: auto;" id="reviewbook">
          <h6 style="margin-left: 0.5rem;">@NAMA ORANG<span style="margin-left: 10px;">haloo</span></h6>
          <div style="background-color: #f2eee3; margin-left: 1.5rem; width: 90%;">
              <p>Belum ada review
              </p>
          </div>
        </div>
  `);
  }
}

async function refreshCard(data){
  let rightSide = $('#cardright');
  rightSide.empty();
  let isbn = data[0].isbn;
  let title = data[0].title;
  let author = data[0].author;
  let year = data[0].year;
  let img = data[0].img;
  rightSide.append(`
    <div style="background-color: #e2c171; display: flex;">
      <img src=${img} class="imgrightside" alt="" style="height: 17rem;">
      <div style="margin-left: 1rem; margin-top: 1rem; background-color: #e2c171;">
        <h5>${title}</h5><br>
        <h7>Author = ${author}</h7><br><br>
        <h7>Year = ${year}</h7><br><br>
        <h7>ISBN = ${isbn}</h7>
      </div>
    </div>
  `);
}

closeightside.addEventListener('click', ()=>{
    rightside.classList.remove('active');
    parentcard.classList.remove('active');
    container.classList.remove('active');
})

function addReview(id) {
  console.log("id = " + id);
  reviewBody = $('#review_body').val();
  $('#review_body').val('');
  console.log("id = " + id);
  $.ajax({
    method: 'POST',
    url: `/daftarbuku/post-book-review/${id}/`,
    headers: {
        'X-CSRFToken': getCsrfToken(),
    },
    data: {
        'review': reviewBody,
    },
    success: function(data) {
      refreshReview(data);
      location.reload();
    },
    error: function(error) {
      console.log("ini id di error = "+id)
      alert('Error on posting comment to server.');
    },
  });
}

function getCsrfToken() {
    return $('#value-csrf-token').text();
}