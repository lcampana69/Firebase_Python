{pkgs}: {
  deps = [
    pkgs.glibcLocales
    pkgs.glibc
    pkgs.postgresql
    pkgs.openssl
  ];
}
