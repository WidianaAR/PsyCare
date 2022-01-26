-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 26 Jan 2022 pada 08.26
-- Versi server: 10.4.21-MariaDB
-- Versi PHP: 8.0.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `psycare`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `admin`
--

CREATE TABLE `admin` (
  `username` varchar(15) NOT NULL,
  `password` varchar(15) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `no_telp` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `admin`
--

INSERT INTO `admin` (`username`, `password`, `nama`, `email`, `no_telp`) VALUES
('rafael', '123', 'Rafa', 'wewe', 12345),
('wardas', '123wr', 'Nanda', 'nanda@gmail.com', 812),
('widia123', '12345', 'Widia', 'widia.war@gmail.com', 2147483647),
('winda', '123wr', 'Nanda', 'nanda@gmail.com', 812);

-- --------------------------------------------------------

--
-- Struktur dari tabel `dokter`
--

CREATE TABLE `dokter` (
  `username` varchar(15) NOT NULL,
  `password` varchar(15) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `no_telp` int(11) NOT NULL,
  `no_sip` int(11) NOT NULL,
  `gelar` varchar(15) NOT NULL,
  `spesialisasi` varchar(50) NOT NULL,
  `jenis_kelamin` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `dokter`
--

INSERT INTO `dokter` (`username`, `password`, `nama`, `email`, `no_telp`, `no_sip`, `gelar`, `spesialisasi`, `jenis_kelamin`) VALUES
('jas', 'mine123', 'Jasmine Zul', 'mine123@gmail.com', 812345689, 2147483647, 'Bachelor\'s Degr', 'Remaja', 'P'),
('say', '1212', 'Widia', 'claura.cn@gmail.com', 81212342, 121232123, 'S1', 'Psikologi Klinis', 'P'),
('widia12389', '890', 'Dicky Zakaria', 'diki.zar@gmail.com', 2147483647, 2147483647, 'Magister', 'Remaja', 'L');

-- --------------------------------------------------------

--
-- Struktur dari tabel `info`
--

CREATE TABLE `info` (
  `id` int(15) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `judul` varchar(50) NOT NULL,
  `isi_info` varchar(10000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `info`
--

INSERT INTO `info` (`id`, `nama`, `judul`, `isi_info`) VALUES
(2, 'Fenny', 'Depresi', 'Depresi adalah suatu kondisi medis berupa perasaan sedih yang berdampak negatif terhadap pikiran, tindakan, perasaan, dan kesehatan mental seseorang.[1] Kondisi depresi adalah reaksi normal sementara terhadap peristiwa-peristiwa hidup seperti kehilangan orang tercinta. Depresi juga dapat merupakan gejala dari sebuah penyakit fisik dan efek samping dari penggunaan obat dan perawatan medis tertentu. Dalam kaitannya dengan gangguan mental lain, depresi dapat juga menjadi gejala dari gangguan kejiwaan seperti Gangguan depresi mayor dan distimia.[2]\r\n\r\nSeseorang dalam kondisi depresi umumnya mengalami perasaan sedih, cemas, atau kosong; mereka juga cenderung merasa terjebak dalam kondisi yang tidak ada harapan, tidak ada pertolongan, penuh penolakan, atau perasaan tidak berharga. Gejala-gejala lain yang mungkin muncul adalah perasaan bersalah, mudah tersinggung, atau kemarahan.[3][4] Lebih jauh, individu yang mengalami depresi dapat juga merasa malu atau gelisah.\r\n\r\nSelain perubahan suasana hati, individu dengan gejala depresi cenderung kehilangan minat untuk melakukan aktivitas-aktivitas yang sebelumnya ia anggap menyenangkan; kehilangan napsu makan atau sebaliknya, makan dengan porsi berlebih. Penderita juga akan kesulitan untuk berkonsentrasi, mengingat detail-detail umum, membuat keputusan, ataupun mengalami kesulitan dalam berhubungan dengan orang lain. Pengalaman-pengalaman ini dapat mendorong individu untuk mencoba bunuh diri.\r\n\r\nSource : id.wikipedia.org'),
(5, 'Manda', 'Skizofrenia', 'Skizofrenia adalah gangguan jiwa yang ditandai dengan gangguan proses berpikir dan tanggapan emosi yang lemah.[1] Keadaan ini pada umumnya diejawantahkan dalam bentuk halusinasi pendengaran, paranoia atau waham yang ganjil, atau cara berbicara dan berpikir yang kacau, dan disertai dengan disfungsi sosial dan pekerjaan yang signifikan. Gejala awal biasanya muncul pada saat dewasa muda, dengan prevalensi semasa hidup secara global sekitar 0,3% – 0,7%.[2] Diagnosis didasarkan atas pengamatan perilaku dan pengalaman penderita yang dilaporkan.\r\n\r\nFaktor penyumbang penting yaitu genetik, lingkungan awal, neurobiologi, serta kondisi psikologis dan proses sosial; beberapa jenis obat resep dan rekreasional sepertinya dapat menjadi penyebab atau kondisi yang memperburuk gejala. Penelitian saat ini difokuskan pada peranan neurobiologi, walaupun tidak ada satupun penyebab organik khusus yang ditemukan. Berbagai kombinasi gejala yang mungkin terjadi telah memicu debat apakah suatu diagnosis mewakili satu kelainan atau beberapa gejala yang berbeda.\r\n\r\nSource : id.wikipedia.org'),
(6, 'Widia', 'Obsesif Kompulsif (OCD)', 'Gangguan obsesif kompulsif (OCD) adalah gangguan mental di mana penderitanya tertekan karena pemikiran yang berulang sehingga menyebabkan penderita tersebut melakukan suatu tindakan secara berulang. Pada dasarnya penderita gangguan ini menyadari bahwa mereka terkena gangguan OCD, tetapi mereka tidak bisa mengontrol dirinya untuk berhenti melakukan tindakan tersebut. Misalnya, seorang penderita OCD akan mencuci tangannya berulang kali karena ia berpikir belum mencuci tangannya dengan bersih.\r\n\r\nSource : id.wikipedia.org');

-- --------------------------------------------------------

--
-- Struktur dari tabel `jadwal_konsul`
--

CREATE TABLE `jadwal_konsul` (
  `id` int(15) NOT NULL,
  `dokter` varchar(50) NOT NULL,
  `pasien` varchar(50) NOT NULL,
  `tanggal` varchar(20) NOT NULL,
  `keterangan` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `jadwal_konsul`
--

INSERT INTO `jadwal_konsul` (`id`, `dokter`, `pasien`, `tanggal`, `keterangan`) VALUES
(4, 'Widia', 'Dew', '20 Desember 2020', 'Konsul Biasa'),
(6, 'Widia', 'Dew', '30 September 2021', 'Biasa'),
(8, 'Widia', 'Dew', '6 Mei 2019', 'B'),
(9, 'widia', 'Dew', '12 Mei 2021', 'konsul biasa');

-- --------------------------------------------------------

--
-- Struktur dari tabel `jadwal_praktik`
--

CREATE TABLE `jadwal_praktik` (
  `nama_dokter` varchar(50) NOT NULL,
  `hari` varchar(10) NOT NULL,
  `jam_awal` varchar(6) NOT NULL,
  `jam_akhir` varchar(6) NOT NULL,
  `id` int(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `jadwal_praktik`
--

INSERT INTO `jadwal_praktik` (`nama_dokter`, `hari`, `jam_awal`, `jam_akhir`, `id`) VALUES
('Widia', 'Rabu', '12.00', '13.00', 5),
('dew', 'selasa', '12.12', '13.13', 23),
('wardas', 'rabu', '12.12', '23.23', 28),
('Widia', 'Kamis', '14.00', '16.00', 29),
('Widia', 'Sabtu', '12.12', '15.15', 30),
('Widia', 'Senin', '12.00', '15.00', 31),
('gina', 'selasa', '', '', 34),
('Jasmin', 'Jumat', '12.00', '14.00', 35);

-- --------------------------------------------------------

--
-- Struktur dari tabel `pasien`
--

CREATE TABLE `pasien` (
  `username` varchar(15) NOT NULL,
  `password` varchar(15) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `no_telp` int(11) NOT NULL,
  `tgl_lahir` varchar(20) NOT NULL,
  `jenis_kelamin` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `pasien`
--

INSERT INTO `pasien` (`username`, `password`, `nama`, `email`, `no_telp`, `tgl_lahir`, `jenis_kelamin`) VALUES
('as', '123', 'Dew', 'stella123@gmail.com', 812343223, '28 Agustus 2001', 'P'),
('intan123', '123', 'Intan Yuningsih', 'intan890@gmail.com', 812234234, '06 Mei 2001', 'P'),
('ryu', '123', 'Shin Ryujin', 'ryujin@gmail.com', 813243234, '4 Mei 2001', 'P');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`username`);

--
-- Indeks untuk tabel `dokter`
--
ALTER TABLE `dokter`
  ADD PRIMARY KEY (`username`);

--
-- Indeks untuk tabel `info`
--
ALTER TABLE `info`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `jadwal_konsul`
--
ALTER TABLE `jadwal_konsul`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `jadwal_praktik`
--
ALTER TABLE `jadwal_praktik`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `pasien`
--
ALTER TABLE `pasien`
  ADD PRIMARY KEY (`username`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `info`
--
ALTER TABLE `info`
  MODIFY `id` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT untuk tabel `jadwal_konsul`
--
ALTER TABLE `jadwal_konsul`
  MODIFY `id` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT untuk tabel `jadwal_praktik`
--
ALTER TABLE `jadwal_praktik`
  MODIFY `id` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
