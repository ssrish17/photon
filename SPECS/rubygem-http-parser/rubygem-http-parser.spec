%global debug_package %{nil}
%global gem_name http-parser

Name:           rubygem-http-parser
Version:        1.2.3
Release:        5%{?dist}
Summary:        An easy-to-use client library for making requests from Ruby.
Group:          Development/Libraries
Vendor:         VMware, Inc.
Distribution:   Photon
URL:            https://rubygems.org/gems/%{gem_name}

Source0: https://rubygems.org/downloads/%{gem_name}-%{version}.gem
%define sha512 %{gem_name}=03c34c3e8174d9010440483af34800b74a7bbddd5daa63607e6aa2254d9c91cf36d90854ea65827b32680432de278aeeb7b8878f788f124c150f163409fa5107

Source1: license.txt
%include %{SOURCE1}

BuildRequires: ruby-devel
BuildRequires: rubygem-ffi-compiler

Requires: rubygem-ffi-compiler
Requires: ruby

%description
An easy-to-use client library for making requests from Ruby. It uses a simple
method chaining system for building requests, similar to Python's Requests.

%prep
%gem_unpack %{SOURCE0}

%build
%gem_build

%install
%gem_install

%files
%defattr(-,root,root,-)
%{gem_base}

%changelog
* Thu Apr 17 2025 Shreenidhi Shedi <shreenidhi.shedi@broadcom.com> 1.2.3-5
- Build gems properly
* Mon Oct 14 2024 Shreenidhi Shedi <shreenidhi.shedi@broadcom.com> 1.2.3-4
- Remove noarch
* Tue Apr 30 2024 Shivani Agarwal <shivani.agarwal@broadcom.com> 1.2.3-3
- Add gem macros
* Wed Feb 28 2024 Shivani Agarwal <shivani.agarwal@broadcom.com> 1.2.3-2
- Update build command, to build with source code
* Fri Oct 20 2023 Shreenidhi Shedi <sshedi@vmware.com> 1.2.3-1
- Initial version.
- Needed by rubygem-http-4.4.1.
