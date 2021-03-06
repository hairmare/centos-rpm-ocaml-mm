Name:     ocaml-mm

Version:  0.4.0
Release:  0.0%{dist}
Summary:  OCAML multimedia library
License:  GPLv2+
URL:      https://github.com/savonet/ocaml-mm
Source0:  https://github.com/savonet/ocaml-mm/releases/download/%{version}/ocaml-mm-%{version}.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-mad
BuildRequires: ocaml-findlib
Requires:      ocaml-mad

%prep
%setup -q 

%build
./configure \
   --prefix=%{_prefix} \
   -disable-ldconf
make all

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}$(ocamlfind printconf destdir)
export OCAMLFIND_LDCONF=ignore
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs

install -d $OCAMLFIND_DESTDIR/%{ocamlpck}
make install

%files
/usr/lib64/ocaml/mm/IO.cmi
/usr/lib64/ocaml/mm/IO.cmo
/usr/lib64/ocaml/mm/IO.cmx
/usr/lib64/ocaml/mm/META
/usr/lib64/ocaml/mm/MIDI.cmi
/usr/lib64/ocaml/mm/MIDI.cmo
/usr/lib64/ocaml/mm/MIDI.cmx
/usr/lib64/ocaml/mm/MIDI.mli
/usr/lib64/ocaml/mm/audio.cmi
/usr/lib64/ocaml/mm/audio.cmo
/usr/lib64/ocaml/mm/audio.cmx
/usr/lib64/ocaml/mm/audio.mli
/usr/lib64/ocaml/mm/dllmm_stubs.so
/usr/lib64/ocaml/mm/image.cmi
/usr/lib64/ocaml/mm/image.cmo
/usr/lib64/ocaml/mm/image.cmx
/usr/lib64/ocaml/mm/image.mli
/usr/lib64/ocaml/mm/libmm_stubs.a
/usr/lib64/ocaml/mm/mm.a
/usr/lib64/ocaml/mm/mm.cma
/usr/lib64/ocaml/mm/mm.cmxa
/usr/lib64/ocaml/mm/ringbuffer.cmi
/usr/lib64/ocaml/mm/ringbuffer.cmo
/usr/lib64/ocaml/mm/ringbuffer.cmx
/usr/lib64/ocaml/mm/ringbuffer.mli
/usr/lib64/ocaml/mm/synth.cmi
/usr/lib64/ocaml/mm/synth.cmo
/usr/lib64/ocaml/mm/synth.cmx
/usr/lib64/ocaml/mm/synth.mli
/usr/lib64/ocaml/mm/video.cmi
/usr/lib64/ocaml/mm/video.cmo
/usr/lib64/ocaml/mm/video.cmx
/usr/lib64/ocaml/mm/video.mli

%description
ocaml-mm is a library dedicated to performing operations on multimedia contents.


%changelog
* Sun Nov 11 2018 Lucas Bickel <hairmare@rabe.ch> - 0.4.0-0.0
- Bump to 0.4.0

* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch> - 0.3.1-1
- initial version, mostly stolen from https://www.openmamba.org/showfile.html?file=/pub/openmamba/devel/specs/ocaml-mm.spec
