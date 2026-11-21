import argparse
import sys
from datetime import date

from pyramid.paster import bootstrap, setup_logging
from sqlalchemy.exc import OperationalError

from .. import models


def setup_models(dbsession):
    """Menambahkan data awal (seeding) mahasiswa dan matakuliah ke database."""
    mahasiswa1 = models.Mahasiswa(
        nim='123',
        nama='Falih',
        jurusan='Teknik Informatika',
        tanggal_lahir=date(2000, 5, 15),
        alamat='Jl. Merdeka No. 123, Lampung',
    )
    mahasiswa2 = models.Mahasiswa(
        nim='129',
        nama='Faiq',
        jurusan='Sistem Informasi',
        tanggal_lahir=date(2001, 8, 22),
        alamat='Jl. Mawar No. 45, Jakarta',
    )

    mk1 = models.Matakuliah(
        kode_mk='IF2110',
        nama_mk='Algoritma dan Struktur Data',
        sks=4,
        semester=3,
    )
    mk2 = models.Matakuliah(
        kode_mk='IF3140',
        nama_mk='Pemrograman Aplikasi Web',
        sks=3,
        semester=5,
    )
    mk3 = models.Matakuliah(
        kode_mk='IF2230',
        nama_mk='Basis Data',
        sks=3,
        semester=4,
    )

    dbsession.add_all([mahasiswa1, mahasiswa2, mk1, mk2, mk3])


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'config_uri',
        help='Configuration file, e.g., development.ini',
    )
    return parser.parse_args(argv[1:])


def main(argv=sys.argv):
    args = parse_args(argv)
    setup_logging(args.config_uri)
    env = bootstrap(args.config_uri)

    try:
        with env['request'].tm:
            dbsession = env['request'].dbsession
            setup_models(dbsession)
            print('Berhasil memasukkan data seeding awal mahasiswa dan matakuliah!')
    except OperationalError:
        print('Pyramid gagal terhubung ke database SQL.')
        print('Pastikan service PostgreSQL berjalan dan connection string di development.ini benar.')


if __name__ == '__main__':
    main()