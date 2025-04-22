%global debug_package %{nil}
%global gemdir %(IFS=: R=($(gem env gempath)); echo ${R[${#R[@]}-1]})
%global gem_name async

Name:           rubygem-async
Version:        2.8.2
Release:        2%{?dist}
Summary:        Async provides a modern asynchronous I/O framework for Ruby, based on nio4r.
Group:          Development/Libraries
Vendor:         VMware, Inc.
Distribution:   Photon
URL:            https://rubygems.org/gems/%{gem_name}/versions/%{version}

Source0:        https://rubygems.org/downloads/%{gem_name}-%{version}.gem
%define sha512 %{gem_name}=9e7861ecb4386d867b994a2544c2690fa10514441b05d6eb6e5aec23bce724b72384ddcfa0fc27d94d6455d11432fac21acb0dc18c5520f940df65c1ceaf2db0

Source1: license.txt
%include %{SOURCE1}

BuildArch: noarch

BuildRequires: ruby-devel
BuildRequires: rubygem-nio4r
BuildRequires: rubygem-timers
BuildRequires: rubygem-fiber-local
BuildRequires: rubygem-console

Requires: rubygem-console >= 1.0.0, rubygem-console < 2.0.0
Requires: rubygem-nio4r >= 2.3.0, rubygem-nio4r < 3.0.0
Requires: rubygem-timers >= 4.1.0, rubygem-timers < 5.0.0
Requires: rubygem-fiber-local
Requires: ruby

%description
Async provides a modern asynchronous I/O framework for Ruby, based on nio4r.
It implements the reactor pattern, providing both IO and timer based events.

%prep
%gem_unpack %{SOURCE0}

%build
%gem_build

%install
%gem_install

%files
%defattr(-,root,root,-)
%{gemdir}

%changelog
*   Thu Apr 17 2025 Shreenidhi Shedi <shreenidhi.shedi@broadcom.com> 2.8.2-2
-   Build gems properly
*   Mon Feb 26 2024 Shivani Agarwal <shivani.agarwal@broadcom.com> 2.8.2-1
-   Update to version 2.8.2
* Wed Oct 18 2023 Shreenidhi Shedi <sshedi@vmware.com> 2.2.1-2
- Fix requires
* Wed Aug 17 2022 Gerrit Photon <photon-checkins@vmware.com> 2.2.1-1
- Automatic Version Bump
* Thu Jul 16 2020 Gerrit Photon <photon-checkins@vmware.com> 1.26.2-1
- Automatic Version Bump
* Wed Aug 21 2019 Stanislav Hadjiiski <hadjiiskis@vmware.com> 1.20.1-1
- Initial build
