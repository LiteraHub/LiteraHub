let hariIni
let batas
var searchInput = document.getElementById("searchInput");

searchInput.addEventListener("input", function () {
    if (searchInput.value === "") {
        refreshItem();
    }
});

let bookId
async function getAll() {
    return fetch("/peminjamanbuku/get-buku-item/").then((res) => res.json())
}

async function getPinjam() {
    return fetch("/peminjamanbuku/get-pinjem/").then((res) => res.json())
}

async function getBuku(id) {
    let url = `/peminjamanbuku/get-buku-by-id/${id}/`;
    return fetch(url).then((res) => res.json());
}

async function getObjek(id) {
    let url = `/peminjamanbuku/get-objek-by-id/${id}/`;
    return fetch(url).then((res) => res.json());
}

async function refreshItem() {
    document.getElementById("product_table").innerHTML = ""
    var kataKunci = document.getElementById("searchInput").value.toLowerCase();
    let all = await getAll()
    let htmlString = ""
    all.forEach((item) => {
        if(!item.fields.title.toLowerCase().includes(kataKunci) && kataKunci != ""){
            return;
        }
        htmlString += `
        <div class="card">
            <div class="card-body">
                <button onclick="openForm(${item.pk})" class="modal-link">
                    <img for="modal-pinjem" src="${item.fields.img}"  class="w-104 h-160" style="object-fit: fill; width: 104px; height: 160px;">
                </button>
            </div>
            <label class="text-sm">${item.fields.title}</label>
        </div>`
    })

    document.getElementById("product_table").innerHTML = htmlString

    document.getElementById("product_dipinjam").innerHTML = ""
    all = await getPinjam()
    htmlString = ""
    all.forEach((item) => {
        htmlString += `
            <div class="card">
                <div class="card-body">
                    <button onclick="openDetail(${item.fields.buku}, ${item.pk})" class="modal-link">
                        <img src="${item.fields.gambarBuku}" class="w-104 h-160" style="object-fit: contain; width: 100%; height: 100%;">
                    </button>
                </div>
                <label class="text-sm">${item.fields.title}</label>
            </div>` 
    })

    document.getElementById("product_dipinjam").innerHTML = htmlString
}

function openForm(id) {
    const modal = document.getElementById('modal');
    modal.classList.remove('hidden');
    bookId = id
}

function closeModal() {
    const modal = document.getElementById('modal');
    document.getElementById("pinjamForm").reset()
    modal.classList.add('hidden'); 
}

function pinjamBuku() {
    let formData = new FormData(document.getElementById('pinjamForm'));
    let tmp = document.getElementById('pinjamForm')
    tanggal_pengembalian_user = new Date(tmp.elements['tanggal_pengembalian'].value);
    nama_user = tmp.elements['nama'].value
    hariIni = new Date()

    if (tanggal_pengembalian_user < hariIni || tanggal_pengembalian_user == "Invalid Date" || nama_user == "") {
        alert("Masukkan input yang valid")    
        document.getElementById("pinjamForm").reset()
        return;
    }

    formData.append('bookId', bookId);
    closeModal()

    fetch("/peminjamanbuku/pinjam_buku/", {
        method: "POST",
        body: formData
    }).then(refreshItem);
        document.getElementById("pinjamForm").reset()
    }

async function openDetail(id, idPinjam) {
    const modalPinjam = document.getElementById('modal-dipinjam');
    let bukuDicari = await getBuku(id)
    let objekPinjam = await getObjek(idPinjam)
    hariIni = new Date()
    batas = new Date(objekPinjam[0].fields.tanggal_pengembalian)
    hariIni.setHours(0,0,0,0)
    batas.setHours(0,0,0,0)


    document.getElementById("informasi-dipinjam").value1 = id
    document.getElementById("informasi-dipinjam").innerHTML = ""
    let htmlString = ""
    htmlString += `
                <div style="display: flex; flex-direction: row; margin-bottom: 3%">
                    <div style="width: 45%; margin-right: 5% ">
                        <img class="drop-shadow-2xl" src="${bukuDicari[0].fields.img}" style="object-fit: contain; width: 100%; height: 90% ;">
                    </div>
                    <div style="width: 75%; display: flex; flex-direction: column;">
                        <div class= "place-content-center">
                            <div class = "place-content-center">
                            <label class= "text-center font-semibold text-xl" style="margin-bottom:4%">Detail Buku</label>
                            </div>
                            <br>
                            <label class= "font-normal" style="margin-bottom:2.5%">Nama Peminjam: ${objekPinjam[0].fields.nama}</label>
                            <br>
                            <label class= "font-normal" style="margin-bottom:2.5%">Tanggal pinjam: ${objekPinjam[0].fields.tanggal_peminjaman}</label>
                            <br>
                            <label class= "font-normal" style="margin-bottom:2.5%">Tanggal kembalikan: ${objekPinjam[0].fields.tanggal_pengembalian}</label>
                            <br>
                            <label class= "font-normal" style="margin-bottom:2.5%">Nama Buku: ${bukuDicari[0].fields.title}</label>
                            <br>
                            <label class= "font-normal" style="margin-bottom:2.5%">Author: ${bukuDicari[0].fields.author}</label>
                            <br>
                            <label class= "font-normal" style="margin-bottom:2.5%">Tahun Terbit: ${bukuDicari[0].fields.year}</label>
                            <br>
                            <label class= "font-normal" style="margin-bottom:2.5%">Isbn: ${bukuDicari[0].fields.isbn}</label>
                        </div>
                    </div>
                </div>
                <div style="display: flex; justify-content: center;">
                    <button onclick="kembalikanBuku()" id="kembalikanButton" type="submit" class="bg-white border-[1px] border-gray-600 rounded px-4 py-2 text-black cursor-pointer hover:bg-blue-700" 
                    style="margin-bottom: 10px;"> Kembalikan </button>
                </div>
                <div style="display: flex; justify-content: center;">                
                    <button onclick="closeDetail()" id="dialog" class="bg-white border-[1px] border-gray-600 rounded px-4 py-2 text-black cursor-pointer hover:bg-gray-600"> Cancel</button>
                </div>` 
    document.getElementById("informasi-dipinjam").innerHTML = htmlString
    refreshItem()
    modalPinjam.classList.remove('hidden');
}

function closeDetail() {
    const modal = document.getElementById('modal-dipinjam');
    modal.classList.add('hidden'); 
}

// TODO: INI BELOM
function kembalikanBuku() {
    if (hariIni > batas){
        alert("TOLONG KEMBALIKAN TEPAT WAKTU LAIN KALI!")
    } else {
        alert("Terima kasih telah meminjam di LiteraHub")
    }
    let id = document.getElementById("informasi-dipinjam").value1
    let formData = new FormData();
    formData.append('bookId', id);
    
    fetch(`/peminjamanbuku/kembalikan-buku/${id}/`, {
    method: "POST",
    body: formData
    }).then(refreshItem);
        closeDetail()
    }


refreshItem()